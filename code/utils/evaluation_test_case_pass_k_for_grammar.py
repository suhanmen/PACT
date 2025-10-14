import os
import json, base64, os, math
import argparse
import datetime
from collections import defaultdict
import sys
import types
import inspect
import multiprocessing
import pdb
import re, ast, math
import csv
from datasets import load_dataset
import random
from tqdm import tqdm
import textwrap
import numpy as np
import csv
from datetime import datetime
from typing import Any, Dict, Set, Tuple
import io, tokenize
import math, heapq, re, itertools, functools
sys.set_int_max_str_digits(0)

_docstring_re = re.compile(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', re.DOTALL)

_error_prefixes = (
    "AssertionError:",
    #"Exception:",
    #"TypeError:",
    #"Timeout",
    #"InvalidInput",
)

_pre_dataset_tag_list = {
        "DeepSeek-R1-Distill-Qwen-14B" : "DeepSeek",
        "Mistral-Nemo-Base-2407" : "Mistral",
        "Qwen3-14B" : "Qwen3",
        "Phi-4-reasoning-plus" : "Phi",
        "chatgpt" : "chatgpt",
        "DeepSeek-R1-Distill-Qwen-14B-SFT" : "DeepSeek-SFT",
        "DeepSeek-R1-Distill-Qwen-14B-RL" : "DeepSeek-RL",
        "Mistral-Nemo-Base-2407-SFT" : "Mistral-SFT",
        "Mistral-Nemo-Base-2407-RL" : "Mistral-RL",
        "Qwen3-14B-SFT" : "Qwen3-SFT",
        "Qwen3-14B-RL" : "Qwen3-RL",
        "Phi-4-reasoning-plus-SFT" : "Phi-SFT",
        "Phi-4-reasoning-plus-RL" : "Phi-RL",
        "gpt-4o-mini" : "gpt-4o-mini",
        "o4-mini" : "o4-mini",
    }
    

def collect_assert_ids_from_source(src: str, base_lineno: int = 1) -> Dict[int, str]:
    tree = ast.parse(src)
    line2id: Dict[int, str] = {}
    class _V(ast.NodeVisitor):
        def __init__(self): self.k = 0
        def visit_Assert(self, node: ast.Assert):
            line2id[base_lineno + node.lineno - 1] = f"a_{self.k}"
            self.k += 1
    _V().visit(tree)
    return line2id

class GrammarRewarder:
    def __init__(self,
                 AVC_weight: float = 0.5,
                 TS_weight : float = 0.5,
                 verbose: bool = False):
        self.W = dict(AVC=AVC_weight, TS=TS_weight)
        self.verbose = verbose

    # ---------- public API -----------------------------------------
    def compute(self,
                task_id: str,
                reference_src: str,
                entry_point  : str,
                parsed_assert_blocks: dict,
                contracts: dict
               ) -> float:
        ns: dict[str, Any] = {}

        exec(compile(reference_src, "<contract_src>", "exec"), ns)
        fn: types.FunctionType = ns[entry_point]
        param_cnt = len(inspect.signature(fn).parameters)
        
        #collect assert-line map
        line2id = collect_assert_ids_from_source(reference_src)
        all_ids = set(line2id.values())

        fired: Dict[str, Dict[str, Any]] = {}
        solution_maps = {}

        for aid, cases in parsed_assert_blocks.items():

            if cases['is_satisfiable'] == False:
                continue
            #print("="*100)
            #print(f"Processing {aid} with {len(cases['solutions'])} cases")
            combination = cases['combination']

            canonical_solution_funcs, solution_map = self.canonical_solution_load_for_one_by_one_contract_check(
                task_id=task_id, 
                contracts=contracts, 
                combination=combination,
                shared_ns=fn.__globals__, 
            )
            
            solution_maps[aid] = solution_map
            
            fired[f"{aid.replace('satisfied_','O: ').replace('violated_','X: ')}"] = {"combination": combination}
            for idx, c in enumerate(cases['solutions']):
                fired[f"{aid.replace('satisfied_','O: ').replace('violated_','X: ')}"][f"test_case_{idx}"] = {}
                raw = c["test_case"]
                
                # AVC
                model_result = run_func_object(fn, raw)
                fired[f"{aid.replace('satisfied_','O: ').replace('violated_','X: ')}"][f"test_case_{idx}"]["full_contract"] = model_result
               
                # TS
                for contract_key, canonical_func in canonical_solution_funcs.items():
                    canonical_result = run_func_object(canonical_func, raw)
                    
                    # # Debugging #########################################################
                    # if canonical_result != "AssertionError: invalid inputs" :
                    #     pdb.set_trace()
                    # #####################################################################
                    
                    fired[f"{aid.replace('satisfied_','O: ').replace('violated_','X: ')}"][f"test_case_{idx}"][f"{contract_key}"] = canonical_result
                    
        if self.verbose:
            for key, value in fired.items():
                print(f"**{key}** : {value}\n")
        
        if fired == {}:
            return 0, {}
        reward, detail = self._compute_grammar_metrics(fired, self.W)
        #print(f"task_id: {task_id}, detail: {detail}")
        return reward, detail
    
    def canonical_solution_load_for_one_by_one_contract_check(
        self,
        task_id: str,
        contracts: dict,
        combination: dict,
        shared_ns: dict | None,  
    ) -> tuple[Dict[str, Any], Dict[str, str]]:
        """Load canonical solution for one-by-one contract check (robust)."""

        if 'humaneval' in task_id.lower():
            jsonl_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
            is_humaneval = True
        elif 'mbpp' in task_id.lower():
            jsonl_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
            is_humaneval = False
        else:
            raise ValueError(f"Unknown benchmark in task_id: {task_id}")

        record = None
        with open(jsonl_path, 'r', encoding='utf-8') as f:
            for line in f:
                j = json.loads(line)
                if j.get('task_id') == task_id:
                    record = j
                    break
        if record is None:
            raise KeyError(f"task_id not found in {jsonl_path}: {task_id}")

        prompt              = record.get('prompt', '')
        full_contract_block = record.get('contract', '')
        canonical_solution  = record.get('canonical_solution', '')
        entry_point         = record.get('entry_point')
        if not entry_point:
            raise KeyError(f"'entry_point' missing for {task_id}")

        selected_pairs = []
        for key, value in combination.items():
            if value is False:
                snippet = contracts.get(key)
                if snippet is None:
                    print(f"⚠️ Contract snippet missing for key={key}")
                    continue
                selected_pairs.append((key, snippet))

        solution_map: Dict[str, str] = {}
        for key, contract_line in selected_pairs:
            if is_humaneval:
                code = f"{prompt}\n{contract_line}\n{canonical_solution}"
                #code = _strip_triple_quoted(code)
            else:
                code = _inject_contracts_into_solution(canonical_solution, contract_line, entry_point)
            solution_map[key] = code

        if shared_ns is not None:
            SAFE_GLOBALS = shared_ns
            if "__builtins__" not in SAFE_GLOBALS:
                SAFE_GLOBALS["__builtins__"] = __builtins__
        else:
            SAFE_GLOBALS = {"__builtins__": __builtins__}

        task_funcs: Dict[str, Any] = {}

        for key, code in solution_map.items():
            local_env: Dict[str, Any] = {}
            try:
                exec(code, SAFE_GLOBALS, local_env)
                fn = local_env.get(entry_point) or SAFE_GLOBALS.get(entry_point)
                if callable(fn):
                    task_funcs[key] = fn
                else:
                    print(f"⚠️ '{entry_point}' not found after exec for key={key}")
            except Exception as e:
                print(f"❌ [{task_id}] exec failed for key={key}: {e}")

        return task_funcs, solution_map
    
    def _is_error(self, res):
        return isinstance(res, str) and res.startswith(_error_prefixes)
    
    
    def _compute_grammar_metrics(self, 
                                 fired: Dict[str, Dict[str, Any]],
                                 w: Dict[str, float]) -> Tuple[float, Dict[str, float]]:
        """Grammar-specific metrics computation."""
        
        avc_scores = []
        ts_scores = []
        
        for section, test_result in fired.items():
            for test_case_index, test_case_result in test_result.items():
                if test_case_index == "combination":
                    continue
                for contract_key, contract_result in test_case_result.items():
                    
                    # Full contract -> AVC (always expect AssertionError + invalid input)
                    if contract_key == "full_contract":
                        model_res = contract_result
                        if all(test_result["combination"].values()):
                            if not self._is_error(model_res):
                                avc_scores.append(1.0)
                            else:
                                avc_scores.append(0.0)
                        else:
                            is_assertion_error = self._is_assertion_error(model_res)
                            avc_scores.append(1.0 if is_assertion_error else 0.0)
                    
                    # Assert contract -> TS (always expect AssertionError + valid input)
                    elif contract_key.startswith("assert_"):
                        if all(test_result["combination"].values()):
                            succ = not self._is_error(contract_result)
                        else:
                            succ = self._is_assertion_error(contract_result)
                        ts_scores.append(1.0 if succ else 0.0)
        
        avc = sum(avc_scores) / len(avc_scores) if avc_scores else 0.0
        ts = (sum(ts_scores) / len(ts_scores)) if ts_scores else None

        if ts is None:
            # No TS evidence → use AVC only
            ts = avc
            tqs = w["AVC"] * avc + w["TS"] * ts
        else:
            tqs = (w["AVC"] * avc + w["TS"] * ts)

        return tqs, dict(AVC=avc, TS=ts, TQS=tqs)

    def _is_assertion_error(self, res) -> bool:
        if isinstance(res, str):
            return res.startswith("AssertionError:")
        return False


def _strip_triple_quoted(src):
    """Replace triple-quoted STRING tokens with '' to keep syntax valid.
    Uses Python tokenizer to avoid breaking code structure; falls back to regex if needed.
    """
    try:
        sio = io.StringIO(src)
        tokens = list(tokenize.generate_tokens(sio.readline))
        new_tokens = []
        for tok in tokens:
            if tok.type == tokenize.STRING:
                s = tok.string
                i = 0
                while i < len(s) and s[i] in 'fFrRuUbB':
                    i += 1
                body = s[i:]
                if body.startswith('"""') or body.startswith("'''"):
                    tok = tokenize.TokenInfo(tok.type, "''", tok.start, tok.end, tok.line)
            new_tokens.append(tok)
        return tokenize.untokenize(new_tokens)
    except Exception:
        return _docstring_re.sub("''", src)

def safe_eval(input_str, repeat_cap=500_000):
    """Safe evaluation of input strings."""
    
    if not isinstance(input_str, str):  
        return input_str
    
    input_str = (input_str
                 .replace("null", "None")
                 .replace("true", "True")
                 .replace("false", "False"))

    input_str = input_str.replace("int.MIN_VALUE", str(-2**31))

    repeat_pat = re.compile(r'^([\'"]).*\1\.repeat\(\d+\)$')
    if repeat_pat.match(input_str):
        s, rest = input_str.split('.repeat(')
        k = int(rest.rstrip(')'))
        if k > repeat_cap:
            print(f"⚠️ repeat length {k} exceeds cap {repeat_cap}")
            return None
        input_str = f"{s} * {k}"

    try:
        return ast.literal_eval(input_str)
    except Exception:
        pass

    SAFE_BUILTINS = {
        "list": list,
        "range": range,
        "float": float,
        "str": str,
        "dict": dict,
        "set": set,          
        "tuple": tuple,
        "complex": complex,
        "frozenset": frozenset,
        "bytearray": bytearray,
        "memoryview": memoryview,
        "iter": iter,
        "bool": bool,
        "int": int,
        "float": float,
        "str": str,
        "dict": dict,
        "set": set,
        "object": object,
        "buffer": memoryview,
        "bytes": bytes,
    }
    SAFE_GLOBALS = {
        "__builtins__": SAFE_BUILTINS,
        "math": math
    }
    try:
        return eval(input_str, SAFE_GLOBALS, {})
    except Exception:
        pass

    if ((input_str.startswith('"') and input_str.endswith('"')) or
        (input_str.startswith("'") and input_str.endswith("'"))):
        return input_str[1:-1]

    return None

def run_func_with_timeout(func, args, timeout=5): 
    """Run a function (code) with a timeout."""
    
    def target(q):
        try:
            result = func(*args)
            q.put(("Success", result))
        except Exception as e:
            q.put(("Exception", type(e).__name__, str(e)))

    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=target, args=(q,))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        p.join()
        return "Timeout"

    if not q.empty():
        msg = q.get()
        if msg[0] == "Success":
            return msg[1]
        elif msg[0] == "Exception":
            return f"{msg[1]}: {msg[2]}"
    return "NoResult"

def summarize_results(results, ks=[1, 10, 100], star_for_1=False):
    """Summarize the results."""
    
    per_task_runs = defaultdict(list)

    for r in results:
        key = (r['task_id'], r['run_index'])
        per_task_runs[key].append(r['success'])

    task2run_success = defaultdict(list)
    for (task_id, run_idx), case_bools in per_task_runs.items():
        task2run_success[task_id].append(all(case_bools))
    total_tasks   = len(task2run_success)
    total_cases   = len(results)
    total_success = sum(row['success'] for row in results)
    total_fail    = total_cases - total_success

    model_exc = sum(1 for r in results if isinstance(r['model_result'], str) and r['model_result'].startswith("Exception"))
    model_to  = sum(1 for r in results if r['model_result'] == "Timeout")
    gt_exc    = sum(1 for r in results if isinstance(r['groundtruth_result'], str) and r['groundtruth_result'].startswith("Exception"))
    gt_to     = sum(1 for r in results if r['groundtruth_result'] == "Timeout")

    # ── pass@k  (any)  ─────────────────────────────────────────
    print("--- Overall pass@k metrics (All runs must pass entire task) ---")
    for k in ks:
        solved = sum(any(run_bools[:k]) for run_bools in task2run_success.values())
        label  = f"pass@{k}"
        if star_for_1 and k == 1:
            label += "*"
        
        if total_tasks == 0:
            print(f"{label}: no tasks found")
            return
        
        print(f"{label}: {solved}/{total_tasks} = {solved/total_tasks:.2%}")

    print("--- Detailed Summary ---")
    print(f"Total Cases (model×task×case): {total_cases}")
    print(f"Success (incl. matching Exceptions/Timeouts): {total_success}")
    print(f"Failure (mismatch): {total_fail}")
    print(f"Model Exception cases: {model_exc}")
    print(f"Model Timeout cases: {model_to}")
    print(f"Groundtruth Exception cases: {gt_exc}")
    print(f"Groundtruth Timeout cases: {gt_to}")

def test_case_load(test_cases_json, data_type):
    """Load test cases."""
    with open(test_cases_json, 'r') as f:
        tc_all = json.load(f)
    test_cases = tc_all['test_cases']
    
    if 'gpt_outputs' in test_cases_json:
        output_dir_root = test_cases_json.split('/')[7]
    else:
        output_dir_root = test_cases_json.split('/')[6]
    dataset_tag = os.path.splitext(os.path.basename(test_cases_json))[0]
    test_cases_model_name= dataset_tag.split("-smt_result")[0]
    return output_dir_root, test_cases, dataset_tag, test_cases_model_name 
    
def _inject_contracts_into_solution(sol, contracts, entry):
    """Inject contracts into the solution."""
    
    if not contracts.strip():
        return sol
    
    pat = rf'^\s*def\s+{re.escape(entry)}\s*\([^)]*\)[^\n]*:'
    m = re.search(pat, sol, flags=re.MULTILINE)
    if not m:
        return sol
    header_end = m.end()
    indent = " " * 0
    indented = textwrap.indent(contracts.rstrip("\n"), indent)
    return sol[:header_end] + "\n" + indented + "\n" + sol[header_end:].lstrip("\n")
    
def canonical_solution_load(output_path, contracts_in):
    """Load canonical solution."""
    
    if 'humaneval' in output_path:
        jsonl_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
    elif 'mbpp' in output_path:
        jsonl_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
    task_funcs = {}

    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            i = json.loads(line)
            
            task_id = i['task_id']
            prompt = i['prompt']
            contract = i['contract']
            canonical_solution = i['canonical_solution']
            entry_point = i.get('entry_point')
            if contracts_in == 'in_contracts':
                if 'humaneval' in output_path:
                    full_code = f"{prompt}\n{contract}\n{canonical_solution}"
                elif 'mbpp' in output_path:
                    full_code = _inject_contracts_into_solution(canonical_solution, contract, entry_point)
            elif contracts_in == 'no_contracts':
                if 'humaneval' in output_path:
                    full_code = f"{prompt}\n{canonical_solution}"
                elif 'mbpp' in output_path:
                    full_code = canonical_solution
            
            local_env = {}
            try:
                exec(full_code, local_env)
                if entry_point not in local_env:
                    print(f"⚠️ {task_id}: '{entry_point}' not found in executed code")
                    continue

                task_funcs[task_id] = local_env[entry_point]
            except Exception as e:
                print(f"❌ [{task_id}] Code execution error: {e}")
                continue

    return task_funcs

def make_json_serializable(obj):
    if obj is ...:
        return None
    if isinstance(obj, dict):
        return {str(k): make_json_serializable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple, set)):
        return [make_json_serializable(v) for v in obj]
    if hasattr(np, 'generic') and isinstance(obj, np.generic):
        return obj.item()
    if 'numpy' in str(type(obj)) and hasattr(obj, 'tolist'):
        return obj.tolist()
    if isinstance(obj, complex):
        return {"real": obj.real, "imag": obj.imag}
    if isinstance(obj, range):
        return list(obj)
    if isinstance(obj, (bytes, bytearray, memoryview)):
        b = bytes(obj)
        try:
            return b.decode('utf-8')
        except UnicodeDecodeError:
            import base64
            return {"$base64": base64.b64encode(b).decode('ascii')}
    try:
        from datetime import datetime, date
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
    except Exception:
        pass
    return obj

def extract_python_code(md):
    """Extract python code from markdown."""
    
    pattern = r'```python\s*(.*?)```'
    blocks = re.findall(pattern, md, re.DOTALL)
    return '\n\n'.join(block.strip() for block in blocks)

def is_assert_case(r):
    """Check if the case is an assert case."""
    
    return isinstance(r['groundtruth_result'], str) and r['groundtruth_result'].startswith("Assert")

def contract_check_save_json(results, output_path):
    """Save contract check results to json with InvalidInput statistics."""
    total_cases = 0
    invalid_input_cases = 0
    
    for task_id, task_data in results.items():
        for section, section_data in task_data.items():
            for contract_key, contract_cases in section_data.items():
                for case in contract_cases:
                    total_cases += 1
                    model_result = case.get("model_result")
                    if isinstance(model_result, str) and "AssertionError:" in model_result:
                        invalid_input_cases += 1
    
    invalid_input_ratio = (invalid_input_cases / total_cases * 100) if total_cases > 0 else 0.0
    
    stats = {
        "statistics": {
            "total_test_cases": total_cases,
            "invalid_input_cases": invalid_input_cases,
            "invalid_input_ratio_percent": round(invalid_input_ratio, 2)
        },
        "contract_check_results": results
    }
    
    with open(output_path, 'w') as f:
        json.dump(stats, f, indent=4, default=make_json_serializable)
        

def canonical_solution_load_for_one_by_one_contract_check(
    output_path: str,
    task_id: str,
    contract_type: str,
    task_type: str,
    model_name: str,
    *,
    debug: bool = False
):
    """Load canonical solution for one-by-one contract check (robust)."""

    if "grammar" in task_type:
        task_mode = "grammar_assert_specification"
    else:
        raise ValueError(f"Unknown task_type: {task_type}")

    if 'humaneval' in output_path.lower():
        jsonl_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
        #if model_name == 'o4-mini':
        contract_path = f'../../code/output_gpt/humaneval/parsing_data/{task_mode}/o4-mini/o4-mini-parsing.json'
        #else:
        #    contract_path = f'../../code/output_base/humaneval/inference/{task_mode}/{model_name}/generated_step_all.json'
        is_humaneval = True
    elif 'mbpp' in output_path.lower():
        jsonl_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
        #if model_name == 'o4-mini':
        contract_path = f'../../code/output_gpt/mbpp/parsing_data/{task_mode}/o4-mini/o4-mini-parsing.json'
        #else:
        #    contract_path = f'../../code/output_base/mbpp/inference/{task_mode}/{model_name}/generated_step_all.json'
        is_humaneval = False
    else:
        raise ValueError(f"output_path must include 'humaneval' or 'mbpp', got: {output_path}")

    record = None

    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            j = json.loads(line)
            if j.get('task_id') == task_id:
                record = j
                break
    if record is None:
        raise KeyError(f"{task_id} not found in {jsonl_path}")

    prompt              = record.get('prompt', '')
    full_contract_block = record.get('contract', '') or ''
    canonical_solution  = record.get('canonical_solution', '')
    entry_point         = record.get('entry_point')
    if not entry_point:
        raise KeyError(f"'entry_point' missing for {task_id}")
    
    contracts_list = parse_contracts_by_assert_blocks(full_contract_block)
    
    # with open(contract_path, 'r', encoding='utf-8') as f:
    #     generated = json.load(f)
        
    # contracts_list = None
    
    # for model_name in generated.keys():
    #     for v in generated[model_name].keys():
    #         if model_name == 'gpt_model':
    #             if v == task_id:
    #                 pdb.set_trace()
    #                 contracts_list = generated[model_name][v]['constraints']
    #                 break
    #         else:
    #             if v.get('task_id') == task_id:
    #                 contracts_list = v.get('contracts_list')
    #                 break
    
    if not isinstance(contracts_list, dict):
        raise KeyError(f"'contracts_list' not found for {task_id} in {contract_path}")
    
    contract_keys = [key for key in contract_type.split(',')[1].split('violated_')[1].split(';')]
    if not contract_keys:
        raise ValueError("contract_type must be non-empty (e.g., {'assert_1': true, 'assert_2': true, 'assert_3': false})")

    full_lines = [ln.rstrip('\n') for ln in full_contract_block.splitlines()]
    selected_pairs = []
    for key in contract_keys:
        snippet = contracts_list.get(key)
        if not snippet:
            if debug:
                print(f"[warn] key '{key}' not in contracts_list")
            continue

        exact = [ln for ln in full_lines if ln.strip() == snippet.strip()]
        if exact:
            selected_pairs.append((key, exact[0]))
        else:
            fuzzy = [ln for ln in full_lines if snippet.strip() in ln.strip()]
            if fuzzy:
                selected_pairs.append((key, fuzzy[0]))
            else:
                if debug:
                    print(f"[warn] No matching line in contract for key '{key}'")

    if not selected_pairs:
        if debug:
            print(f"[info] No contracts matched for {task_id} with keys={contract_keys}")
        return {task_id: {}}, "All contracts are true"

    solution_map = {}

    for key, contract_line in selected_pairs:
        if is_humaneval:
            code = f"{prompt}\n{contract_line}\n{canonical_solution}"
            #code = _strip_triple_quoted(code)
        else:
            code = _inject_contracts_into_solution(canonical_solution, contract_line, entry_point)
        solution_map[key] = code
    
    task_funcs = {task_id: {}}
    SAFE_GLOBALS = {
        "__builtins__": __builtins__
    }
    for key, code in solution_map.items():
        local_env = {}
        try:
            exec(code, SAFE_GLOBALS, local_env)
            fn = local_env.get(entry_point)
            if callable(fn):
                task_funcs[task_id][key] = fn
            else:
                msg = f"'{entry_point}' not found after exec for {key}"
                print("⚠️", msg)
                
        except Exception as e:
            print(f"❌ [{task_id}] exec failed for {key}: {e}")
    
    if code == None:
        code = "All contracts are true"

    return task_funcs, solution_map

### Use another python file for reward
def canonical_solution_load_for_reward(dataset_tag, contracts_in="no_contracts"):
    """Load canonical solution for reward. Use another python file for reward."""
    
    if 'humaneval' in dataset_tag.lower():
        jsonl_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
    elif 'mbpp' in dataset_tag.lower():
        jsonl_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
    else:
        raise ValueError("dataset_tag must contain 'humaneval' or 'mbpp'")

    task_map = {}
    with open(jsonl_path, encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            task_id       = rec["task_id"]
            prompt        = rec["prompt"]
            contract      = rec["contract"]
            canonical_src = rec["canonical_solution"]
            entry_point   = rec["entry_point"]

            if contracts_in == "in_contracts":
                if 'humaneval' in dataset_tag:
                    full_code = f"{prompt}\n{contract}\n{canonical_src}"
                else:  # MBPP
                    full_code = _inject_contracts_into_solution(
                        canonical_src, contract, entry_point
                    )
            else:  # no_contracts
                full_code = f"{prompt}\n{canonical_src}" if 'humaneval' in dataset_tag \
                            else canonical_src
            
            if task_id == 'HumanEval/64':
                clean_code = full_code
            else:
                clean_code = _strip_triple_quoted(full_code)

            local_env = {}
            try:
                exec(clean_code, local_env)
                func_obj = local_env[entry_point]
                task_map[task_id] = (func_obj, clean_code, entry_point)
            except Exception as e:
                print(f"[skip] {task_id}: {e}")
    return task_map

### Pass@k Score
def collapse_case_runs(case_runs_dict):
    """Collapse case runs."""
    
    per_task_runs = defaultdict(list)
    for (tid, section, case_idx), case_succs in case_runs_dict.items():
        if case_succs:
            per_task_runs[tid].append(all(case_succs))
    return per_task_runs

def collapse_case_runs_2(case_runs_dict):
    per_task_runs = defaultdict(list)
    for (tid, run_idx), case_succs in case_runs_dict.items():
        if case_succs:
            per_task_runs[tid].append(all(case_succs))
    return per_task_runs

### Groundtruth code play
def run_func_object(func, input_args):
    """Run a function object with input arguments."""
    try:
        sig = inspect.signature(func)
        param_count = len(sig.parameters)

        if isinstance(input_args, dict):
            param_names = list(sig.parameters.keys())
            if param_count == 1:
                if param_names[0] in input_args:
                    args_to_pass = [input_args[param_names[0]]]
                else:
                    return "InvalidInput"
            else:
                # if there are multiple parameters, then we need to pass the values in order as a list
                args_to_pass = []
                for param_name in param_names:
                    if param_name in input_args:
                        args_to_pass.append(input_args[param_name])
                    else:
                        return "InvalidInput"
            return run_func_with_timeout(func, args_to_pass, timeout=5)
    
    except AssertionError as e:
        return f"Exception: {e}"

    except Exception as e:
        return f"Exception: {e}"

### our test case
def run_test_file(file_path, input_args, model_name=None, test_cases_json=None):
    """Run a test file with input arguments."""
    local_env = {}
    try:
        with open(file_path, 'r') as f:
            code_str = f.read()
            
        if '```python' in code_str:
            code_str = extract_python_code(code_str)
        exec(code_str, local_env)

        func_candidates = [v for v in local_env.values() if isinstance(v, types.FunctionType)]
        if not func_candidates:
            print(f"⚠️ No valid function found in {file_path}")
            return "NoFunction"
        func = func_candidates[0]

        sig = inspect.signature(func)
        param_count = len(sig.parameters)

        parsed_args = safe_eval(input_args)
        
        if parsed_args is None:
            print(f"⚠️ Skipping case due to safe_eval failure: {input_args}")
            return "InvalidInput"

        """This is for the case that the input is a list or tuple."""
        if param_count == 1:
            if isinstance(parsed_args, (list, tuple)) and len(parsed_args) == 1:
                args_to_pass = [parsed_args[0]]
            else:
                args_to_pass = [parsed_args]
        else:
            if isinstance(parsed_args, (list, tuple)):
                args_to_pass = parsed_args
            else:
                args_to_pass = [parsed_args]

        result = run_func_with_timeout(func, args_to_pass, timeout=5)
        return result
    
    except AssertionError as e:
        #return f"AssertionError: {e}"
        return f"Exception: {e}"

    except Exception as e:
        return f"Exception: {e}"

### Assert-based testcases
def run_func_with_tests(func, test_code):
    """Run a function with tests."""
    try:
        env = {'__builtins__': __builtins__}
        if not isinstance(func, types.FunctionType):
            return "InvalidFunction"

        env[func.__name__] = func

        res = run_func_with_timeout(
            lambda c=compile(test_code, "<humaneval_test>", "exec"): exec(c, env), [], timeout=5
        )
        return "Pass" if res is None else res

    except AssertionError as e:
        #return f"AssertionError: {e}"
        return f"Exception: {e}"

    except Exception as e:
        return f"Exception: {e}"

def run_file_with_tests(py_path, test_code):
    """Run a file (~*.py) with tests."""
    try:
        env = {}
        with open(py_path, "r") as f:
            exec(f.read(), env)

        res = run_func_with_timeout(
            lambda c=compile(test_code, "<humaneval_test>", "exec"): exec(c, env), [], timeout=5
        )
        return "Pass" if res is None else res
    except AssertionError as e:
        return f"AssertionError: {e}"
    except Exception as e:
        return f"Exception: {e}"

### Evaluate the model
def evaluate(models_base_dir, model_names, test_cases_json, output_path, data_type, mode):
    """Evaluate the model."""
    output_dir_root, test_cases, dataset_tag, test_cases_model_name = test_case_load(test_cases_json, data_type)
    canonical_solution_code = canonical_solution_load(output_path, 'in_contracts')
    canonical_solution_code_no_contracts = canonical_solution_load(output_path, 'no_contracts')
    
    if 'output_our' in test_cases_json and 'SFT' in test_cases_json:
        dataset_tag = f"{dataset_tag}-SFT"
    elif 'output_our' in test_cases_json and 'RL' in test_cases_json:
        dataset_tag = f"{dataset_tag}-RL"
    
    pre_dataset_tag_list = _pre_dataset_tag_list
    
    post_dataset_tag_list = {
        'DeepSeek_pre_filtering_results' : 'DeepSeek',
        'Mistral_pre_filtering_results' : 'Mistral',
        'Qwen_pre_filtering_results' : 'Qwen',
        'Phi_pre_filtering_results' : 'Phi',
        'chatgpt_pre_filtering_results' : 'chatgpt',
        'SFT-DeepSeek_pre_filtering_results' : 'SFT-DeepSeek',
        'RL-DeepSeek_pre_filtering_results' : 'RL-DeepSeek',
        'SFT-Mistral_pre_filtering_results' : 'SFT-Mistral',
        'RL-Mistral_pre_filtering_results' : 'RL-Mistral',
        'SFT-Qwen_pre_filtering_results' : 'SFT-Qwen',
        'RL-Qwen_pre_filtering_results' : 'RL-Qwen',
        'SFT-Phi_pre_filtering_results' : 'SFT-Phi',
        'RL-Phi_pre_filtering_results' : 'RL-Phi',
        'gpt-4o-mini_pre_filtering_results' : 'gpt-4o-mini',
        'o4-mini_pre_filtering_results' : 'o4-mini',
    }

    if dataset_tag.split("-smt_result")[0] in pre_dataset_tag_list.keys():
        dataset_tag = pre_dataset_tag_list[dataset_tag.split("-smt_result")[0]]
    elif dataset_tag.split("_filtered")[0] in post_dataset_tag_list.keys():
        dataset_tag = post_dataset_tag_list[dataset_tag.split("_filtered")[0]]

    assert_fail_len = 0
    for model_name in model_names:
        results = [] 
        contract_check_results = {}   
        print(f"=== Evaluating Model: {model_name} ===")
        
        if model_name != 'ground_truth':
            model_dir = os.path.join(models_base_dir, model_name)
        
        if 'filtered' in test_cases_json:
            model_out = os.path.join(output_path, 'post_filtering', model_name, output_dir_root, dataset_tag)
        else:
            model_out = os.path.join(output_path, mode, output_dir_root, dataset_tag) # Save root

        print(f"Output path: {model_out}")
        os.makedirs(model_out, exist_ok=True)
        
        # extract temperature 
        try:
            temp = float(model_name.split('_temp_')[-1])
        except:
            if model_name == 'ground_truth':
                temp = 0.0
            else:
                temp = None
                
        # 0.0 → 1_time, other → 100_time
        MAX_K = 1 if temp == 0.0 else 100    
        # pass@k 
        per_task_runs = defaultdict(list)    
        # {task_id: [bool, bool, ...]}  
        per_task_runs_contract = defaultdict(list)  
        per_task_runs_func     = defaultdict(list)
        
        tqdm_nums = []
        for tqdm_num in test_cases.keys():
            if test_cases[tqdm_num] != {}:
                tqdm_nums.append(tqdm_num)
        
        for run_idx in range(MAX_K):
            print(f"▶ Run {run_idx + 1}/{MAX_K}")
            if test_cases == {}:
                print("**************No test cases found**************")
                exit()
            for task_id, raw in tqdm(test_cases.items(), total=len(tqdm_nums), desc=f"[{model_name}] Tasks", leave=False):
                
                # # Debugging #########################################################
                # if task_id != "HumanEval/144":
                #     continue
                # #####################################################################
                
                contract_check_results[task_id] = {}

                if isinstance(raw, list):
                    grouped = defaultdict(list)
                    for case in raw:
                        grouped[case.get('section', 'all')].append(case)
                else:
                    grouped = raw
                
                if model_name == 'ground_truth':
                    model_py = 'ground_truth'
                else:
                    if 'humaneval' in data_type or 'HumanEvalPlus.jsonl' in data_type:
                        he_folder = os.path.join(model_dir, f"HumanEval_{task_id.split('/')[1]}")
                    elif 'mbpp' in data_type or 'MbppPlus.jsonl' in data_type:
                        he_folder = os.path.join(model_dir, f"Mbpp_{task_id.split('/')[1]}")
                    
                    if temp == 0.0:
                        model_py = os.path.join(he_folder, "0.py")
                        if not os.path.exists(model_py):
                            print(f"⚠️ {model_py} not found"); pdb.set_trace()
                    else:
                        cands = [os.path.join(he_folder, f) for f in os.listdir(he_folder) if f.endswith('.py')]
                        if not cands:
                            model_py = "FileNotFound"; pdb.set_trace()
                        else:
                            model_py = random.choice(cands)

                # Test case all passed
                task_success = True 
                
                # test case
                for section, cases in grouped.items():
                    # This means that smt solver failed to find a solution
                    contract_check_results[task_id][section] = {}
                    
                    if cases['is_satisfiable'] == False:
                        continue
                    
                    # We only checking the violated cases
                    if section.split('violated_')[1] == '':
                        continue
          
                    for idx, case in enumerate(cases['solutions'], start=1):
                        
                        # Aseert mode - check one by one contract
                        if 'assert_specification' in test_cases_json:
                            canonical_solution_code_for_one_by_one_contract_check, solution_map = canonical_solution_load_for_one_by_one_contract_check(output_path, task_id, section, data_type, test_cases_model_name)
                            for contract_in_key, solutions in canonical_solution_code_for_one_by_one_contract_check.items():
                                for solution_key, solution in solutions.items():
                                    if contract_in_key not in contract_check_results[task_id][section]:
                                        contract_check_results[task_id][section][contract_in_key] = []
                                    inp        = case["test_case"]
                                    model_res  = run_func_object(solution, inp)
                                     
                                    contract_check_results[task_id][section][contract_in_key].append({
                                        "case_index":         idx,
                                        "contract_in_key":    solution_key,
                                        "code":               solution_map[solution_key],
                                        "input":              inp,
                                        "model_result":       model_res,
                                    })
    
                        # Pre-filtering: checking the ground truth both with and without contracts
                        if model_name == 'ground_truth':
                            inp        = case["test_case"]
                            gt_res     = run_func_object(canonical_solution_code.get(task_id), inp)
                            model_res  = run_func_object(canonical_solution_code_no_contracts.get(task_id), inp)
                            assert_cnt = 1
                        
                        # Post-filtering
                        # elif "input" in case:
                        #     inp        = case["input"]
                        #     gt_res     = run_func_object(canonical_solution_code.get(task_id), inp)
                        #     model_res  = run_test_file(model_py, inp, model_name, test_cases_json)
                        #     assert_cnt = 1  
                        
                        # Assert-based testcases: 
                        # else:
                        #     tcode      = case["test_code"]
                        #     gt_res     = run_func_with_tests(canonical_solution_code.get(task_id), tcode)
                        #     model_res  = run_file_with_tests(model_py, tcode)
                        #     assert_cnt = sum(1 for line in tcode.splitlines() if line.lstrip().startswith("assert"))
                        
                        if (model_res == "Timeout" and gt_res == "Timeout") \
                        or (isinstance(model_res, str) and model_res.startswith("Exception") and isinstance(gt_res, str) and gt_res.startswith("Exception")) \
                        or (isinstance(model_res, str) and model_res.startswith("TypeError") and isinstance(gt_res, str) and gt_res.startswith("TypeError")):
                            succ = True
                        else:
                            succ = (model_res == gt_res)
                        
                        if not succ:
                            task_success = False
                            if isinstance(gt_res, str) and gt_res.startswith('Assert'):
                                assert_fail_len += 1
                        
                        results.append({
                            "model":              model_name,
                            "py_file":            model_py,
                            "task_id":            task_id,
                            "section":            section,
                            "case_index":         idx,
                            "run_index":          run_idx,
                            "success":            succ,
                            "input":              inp,
                            "model_result":       model_res,
                            "groundtruth_result": gt_res,
                            "assert_cnt":    assert_cnt,
                        })

            per_task_runs[task_id].append(task_success)

        contract_check_save_json(contract_check_results, os.path.join(model_out, f"{dataset_tag}_contract_check_results.json"))

        # contract test case -> functionality + contracts error (assertion error)
        # functionality test case -> functionality
        combined_case_results = defaultdict(lambda: {'contract': [], 'functionality': []})
        
        # assertion error pattern
        assertion_pattern = re.compile(r'^AssertionError:')
        # All *Error: pattern
        error_pattern = re.compile(r'^(?:[A-Za-z_]\w*Error|Exception):')
        
        for r in results:       
            key = (r['task_id'], r['section'], r['case_index'])
            gt_res    = str(r['groundtruth_result'])
            model_res = str(r['model_result'])
            
            # if input is empty -> pass
            if r.get('input') == None or r.get('input') == '' or (gt_res == None or model_res == None) or (gt_res == 'None' or model_res == 'None') or (gt_res == 'Timeout' and model_res == 'Timeout') or (gt_res == 'InvalidInput' and model_res == 'InvalidInput'):
                continue
            
            # Ground truth -> AssertionError case
            is_gt_assert = bool(assertion_pattern.match(gt_res))
            # Ground truth -> All *Error: pattern
            is_gt_error    = bool(error_pattern.match(gt_res))
            # Model -> All *Error: pattern
            is_model_error = bool(error_pattern.match(model_res))

            # filtering contract test case
            if is_gt_assert and not is_model_error: 
                combined_case_results[key]['contract'].append(model_res == gt_res)
            # filtering functionality test case
            elif (not is_gt_error) and (not is_model_error) : 
                combined_case_results[key]['functionality'].append(model_res == gt_res)

        # contract pass@k
        per_task_runs_contract = collapse_case_runs({k: v['contract'] for k, v in combined_case_results.items()})
        # functionality pass@k
        per_task_runs_func     = collapse_case_runs({k: v['functionality'] for k, v in combined_case_results.items()})
        
        contract_case_results = defaultdict(list)
        func_case_results     = defaultdict(list)
        for r in results:
            key = (r['task_id'], r['run_index'])
            if is_assert_case(r):
                contract_case_results[key].append(r['success'])
            else:
                func_case_results[key].append(r['success'])
        per_task_runs_contract_2 = collapse_case_runs_2(contract_case_results)
        per_task_runs_func_2     = collapse_case_runs_2(func_case_results)
            
        # pass@k CSV save
        def compute_pass_at_k_dict(runs_dict, tag):
            result = {}
            for k in [1, 10, 100] if temp != 0.0 else [1]:
                solved = sum(any(runs[:k]) for runs in runs_dict.values())
                key = f"{tag}pass@{k}" if not (k == 1 and temp == 0.0) else f"{tag}pass@1*"
                result[key] = (solved, len(runs_dict), solved / len(runs_dict) if runs_dict else 0.0)
            return result
        
        # filtering results
        metrics_contract = compute_pass_at_k_dict(per_task_runs_contract, tag='Contracts-')
        metrics_func = compute_pass_at_k_dict(per_task_runs_func, tag='Functionality-')
        metrics = {**metrics_contract, **metrics_func}
        order = list(metrics_contract.keys()) + list(metrics_func.keys())
        os.makedirs(output_path, exist_ok=True)
        csv_path = os.path.join(model_out, f"{dataset_tag}_{mode}_pass_at_k.csv")
        with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)
            writer.writerow(['metric', 'solved', 'total_tasks', 'rate'])
            for key in order:
                s, tot, r = metrics[key]
                writer.writerow([key, s, tot, f"{r:.2%}"])
                
        # all results
        metrics_all_2 = compute_pass_at_k_dict(per_task_runs, tag='All-')   
        metrics_contract_2 = compute_pass_at_k_dict(per_task_runs_contract_2, tag='Contracts-')
        metrics_func_2 = compute_pass_at_k_dict(per_task_runs_func_2, tag='Functionality-')
        metrics_2  = {**metrics_all_2, **metrics_contract_2, **metrics_func_2}
        order = list(metrics_all_2.keys()) + list(metrics_contract_2.keys()) + list(metrics_func_2.keys())
        os.makedirs(output_path, exist_ok=True)
        csv_path = os.path.join(model_out, f"{dataset_tag}_all_pass_at_k.csv")
        with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)
            writer.writerow(['metric', 'solved', 'total_tasks', 'rate'])
            for key in order:
                s, tot, r = metrics_2[key]
                writer.writerow([key, s, tot, f"{r:.2%}"])
                

        # 1. total test cases
        total_test_cases = len(results)
        # 2. failed test cases 
        total_failed_test_cases = len([r for r in results if not r['success']])
        # 3. assert related statistics
        total_assert_cases = [r for r in results if is_assert_case(r)]
        non_assert_cases = [r for r in results if not is_assert_case(r)]
        
        assert_len = len(total_assert_cases)
        assert_fail_len = len([r for r in total_assert_cases if not r['success']])
        analysis_csv = os.path.join(model_out, f"{dataset_tag}_all_results_analysis_output.csv")
        
        non_assert_total = len(non_assert_cases)
        non_assert_success = len([r for r in non_assert_cases if not r['success']])

        subset = results
        
        unique_task_ids = {r['task_id'] for r in subset}
        num_tasks = len(unique_task_ids)
        with open(analysis_csv, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)
            writer.writerow(['Metric', 'Count'])
            writer.writerow(['Total test cases', total_test_cases])
            writer.writerow(['Total failed test cases', total_failed_test_cases])
            writer.writerow(['Total passed ratio (overall)', f"{((total_test_cases - total_failed_test_cases) / total_test_cases * 100):.3f}%" if total_test_cases else "0.00%"])
            writer.writerow(['Assert ratio (of all failed testcases)', f"{(assert_len / total_test_cases * 100):.3f}%" if total_test_cases else "0.00%"])
            writer.writerow(['', ''])
            writer.writerow(['Contracts Test Cases', ''])
            writer.writerow(['Total contracts testcases (GT)', assert_len])
            writer.writerow(['Failed contracts testcases (GT)', assert_fail_len])
            writer.writerow(['Failed ratio (of contracts)', f"{(assert_fail_len / assert_len * 100):.3f}%" if assert_len else "0.00%"])
            writer.writerow(['', ''])
            writer.writerow(['Functionality Test Cases', ''])
            writer.writerow(['Total functionality testcases', non_assert_total])
            writer.writerow(['Failed functionality testcases', non_assert_success])
            writer.writerow(['Failed ratio (functionality only)', f"{(non_assert_success / non_assert_total * 100):.3f}%" if non_assert_total else "0.00%"])
            writer.writerow(['', ''])
            writer.writerow(['Total tasks', num_tasks])
            
        star = model_names[0].split('_temp_')[-1] == '0.0'
        summarize_results(results, ks=[1, 10, 100], star_for_1=star)

        with open(os.path.join(model_out, f"{dataset_tag}_all_results.json"), 'w') as f:
            cleaned = make_json_serializable(subset)
            json.dump(cleaned, f, indent=2)
        
        if subset:
            with open(os.path.join(model_out, f"{dataset_tag}_all_results.csv"), 'w', newline='', encoding='utf-8') as cf:
                try:
                    writer = csv.DictWriter(cf, fieldnames=subset[0].keys())
                    writer.writeheader()
                    writer.writerows(subset)
                except:
                    writer = csv.DictWriter(cf,fieldnames=subset[0].keys(), quoting=csv.QUOTE_MINIMAL, doublequote=True,   escapechar="\\")
                    writer.writeheader()
                    writer.writerows(subset)
                
                
        # save combined results task_id
        valid_runs     = set(combined_case_results.keys())
        combined_subset = [r for r in subset if (r['task_id'], r['section'], r['case_index']) in valid_runs]
        
        # contract/functionality task_id analysis_output
        combined_analysis_csv = os.path.join(model_out, f"{dataset_tag}_{mode}_analysis_output.csv")
        total_test_cases         = len(combined_subset)
        total_failed_test_cases  = len([r for r in combined_subset if not r['success']])
        total_assert_cases       = [r for r in combined_subset if is_assert_case(r)]
        non_assert_cases         = [r for r in combined_subset if not is_assert_case(r)]
        assert_len = len(total_assert_cases)
        assert_fail_len = len([r for r in total_assert_cases if not r['success']])
        non_assert_total = len(non_assert_cases)
        non_assert_success = len([r for r in non_assert_cases if not r['success']])
        unique_task_ids_combined = {r['task_id'] for r in combined_subset}
        num_tasks_combined       = len(unique_task_ids_combined)
        unique_task_ids_contract = set(per_task_runs_contract.keys())
        num_tasks_contract_combined       = len(unique_task_ids_contract)
        unique_task_ids_func     = set(per_task_runs_func.keys())
        num_tasks_func_combined           = len(unique_task_ids_func)
        with open(combined_analysis_csv, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)
            writer.writerow(['Metric', 'Count'])
            writer.writerow(['Total test cases', total_test_cases])
            writer.writerow(['Total failed test cases', total_failed_test_cases])
            writer.writerow(['Total passed ratio (overall)', f"{((total_test_cases - total_failed_test_cases) / total_test_cases * 100):.3f}%" if total_test_cases else "0.00%"])
            writer.writerow(['Assert ratio (of all failed testcases)', f"{(assert_len / total_test_cases * 100):.3f}%" if total_test_cases else "0.00%"])
            writer.writerow(['', ''])
            writer.writerow(['Contracts Test Cases', ''])
            writer.writerow(['Total contracts testcases (GT)', assert_len])
            writer.writerow(['Failed contracts testcases (GT)', assert_fail_len])
            writer.writerow(['Failed ratio (of contracts)', f"{(assert_fail_len / assert_len * 100):.3f}%" if assert_len else "0.00%"])
            writer.writerow(['', ''])
            writer.writerow(['Functionality Test Cases', ''])
            writer.writerow(['Total functionality testcases', non_assert_total])
            writer.writerow(['Failed functionality testcases', non_assert_success])
            writer.writerow(['Failed ratio (functionality only)', f"{(non_assert_success / non_assert_total * 100):.3f}%" if non_assert_total else "0.00%"])
            writer.writerow(['', ''])
            writer.writerow(['Total tasks', num_tasks_combined])
            writer.writerow(['Total contract tasks', num_tasks_contract_combined])
            writer.writerow(['Total functionality tasks', num_tasks_func_combined])
            
        with open(os.path.join(model_out, f"{dataset_tag}_{mode}_results.json"), 'w') as f:
            cleaned = make_json_serializable(combined_subset)
            json.dump(cleaned, f, indent=2)
        
        indices = [
            {"task_id": r["task_id"], "section": r["section"], "case_index": r["case_index"]}
            for r in combined_subset
        ]

        data = test_cases
        model_key = test_cases_model_name

        # filtering structure
        if (test_cases_json != '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl' and 
            test_cases_json != '../../data/mbppplus-0.2.0/MbppPlus.jsonl'):
            filtered = {}
            for idx in indices:
                task = idx['task_id']           # e.g. "HumanEval/3"
                section = idx['section']        # e.g. "assert_1"
                # case_index is 1-based -> 0-based
                ci = idx['case_index'] - 1

                # nested dict initialize
                filtered.setdefault(task, {})
                filtered[task].setdefault(section, [])

                # extract corresponding entry
                entries = data.get(task, {}).get(section, [])
                if 0 <= ci < len(entries['solutions']):
                    filtered[task][section].append(entries['solutions'][ci])

            # final structure and file write
            out = {model_key: filtered}
            with open(os.path.join(model_out,f"{dataset_tag}_{mode}_results_filtered.json"), 'w', encoding='utf-8') as f:
                json.dump(out, f, ensure_ascii=False, indent=2)
                    
            if combined_subset:
                with open(os.path.join(model_out, f"{dataset_tag}_{mode}_results.csv"), 'w', newline='', encoding='utf-8') as cf:                    
                    try:
                        writer = csv.DictWriter(cf, fieldnames=combined_subset[0].keys())
                        writer.writeheader()
                        writer.writerows(combined_subset)
                    except:
                        writer = csv.DictWriter(cf,fieldnames=combined_subset[0].keys(), quoting=csv.QUOTE_MINIMAL, doublequote=True,   escapechar="\\")
                        writer.writeheader()
                        writer.writerows(combined_subset)
                
                    
                    

        # contract/functionality filtered structure
        def save_filtered_json(subset, out_path):
            indices = [
                {"task_id": r["task_id"], "section": r["section"], "case_index": r["case_index"]}
                for r in subset
            ]
            filtered = {}
            for idx in indices:
                task = idx['task_id']
                section = idx['section']
                ci = idx['case_index'] - 1
                filtered.setdefault(task, {})
                filtered[task].setdefault(section, [])
                
                entries = test_cases.get(task, {}).get(section, [])
                if 0 <= ci < len(entries['solutions']):
                    filtered[task][section].append(entries['solutions'][ci])
            out = {test_cases_model_name: filtered}
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(out, f, ensure_ascii=False, indent=2)

        # contract subset save (filtered structure)
        if mode == 'pre_filtering':
            combined_subset_contract = [
                r for r in subset
                if (r['task_id'], r['section'], r['case_index']) in combined_case_results
                and combined_case_results[(r['task_id'], r['section'], r['case_index'])]['contract']
            ]
            save_filtered_json(combined_subset_contract, os.path.join(model_out, f"{dataset_tag}_{mode}_contracts_results_filtered.json"))

            combined_subset_func = [
                r for r in subset
                if (r['task_id'], r['section'], r['case_index']) in combined_case_results
                and combined_case_results[(r['task_id'], r['section'], r['case_index'])]['functionality']
            ]
            save_filtered_json(combined_subset_func, os.path.join(model_out, f"{dataset_tag}_{mode}_functionality_results_filtered.json"))

        if subset:
            task_stats = defaultdict(lambda: {'succ': 0, 'fail': 0})
            if data_type not in ['humaneval','humanevalplus']:
                for row in subset:
                    if row['success']:
                        task_stats[row['task_id']]['succ'] += 1
                    else:
                        task_stats[row['task_id']]['fail'] += 1
            else:
                for row in subset:
                    tid = row['task_id']            # current task id
                    cnt = row.get('assert_cnt', 1)  # assert based -> line count, not assert based -> 1

                    if row['success']:
                        task_stats[tid]['succ'] = cnt   # replace += with =
                        task_stats[tid]['fail'] = 0     # opposite item is 0
                    else:
                        task_stats[tid]['succ'] = 0
                        task_stats[tid]['fail'] = cnt
            
            sum_csv = os.path.join(model_out, f"{dataset_tag}_all_per_task_summary.csv")
            with open(sum_csv, 'w', newline='', encoding='utf-8') as cf:
                w = csv.writer(cf)

                header = ['task_id', 'success_cnt', 'fail_cnt', 'total', 'success_rate']
                if temp == 0.0:
                    header.append('pass@1*')
                else:
                    header.extend(['pass@1', 'pass@10', 'pass@100'])
                w.writerow(header)

                for task_id in sorted(task_stats, key=lambda x: int(x.split('/')[1])):
                    s = task_stats[task_id]['succ']
                    f = task_stats[task_id]['fail']
                    tot = s + f
                    rate = f"{(s / tot):.2%}" if tot else "0.00%"

                    # pass@k calculation (per_task_runs is already filled)
                    runs = per_task_runs.get(task_id, [])     # length = MAX_K
                    if temp == 0.0:                           # k=1* only
                        p1 = int(any(runs[:1]))
                        row = [task_id, s, f, tot, rate, p1]
                    else:                                     # k=1·10·100
                        p1   = int(any(runs[:1]))
                        p10  = int(any(runs[:10]))
                        p100 = int(any(runs[:100]))
                        row = [task_id, s, f, tot, rate, p1, p10, p100]

                    w.writerow(row)
            print(f"📁 per-task summary CSV saved → {sum_csv}")
    
    print(f"✅ All evaluation completed. Results are saved in {output_path}\n\n")

def save_path_for_evaluation(test_cases_json, output_path, mode, model_name):
        

    if 'gpt_outputs' in test_cases_json:
        output_dir_root = test_cases_json.split('/')[7]
    else:
        output_dir_root = test_cases_json.split('/')[6]

    dataset_tag = os.path.splitext(os.path.basename(test_cases_json))[0]
    
    pre_dataset_tag_list = _pre_dataset_tag_list
    if dataset_tag.split("-smt_result")[0] in pre_dataset_tag_list.keys():
        dataset_tag = pre_dataset_tag_list[dataset_tag.split("-smt_result")[0]]
        model_out = os.path.join(output_path, mode, output_dir_root, dataset_tag) # Save root

    return model_out


def parse_contracts_by_assert_blocks(contract_text):
    lines = [line for line in contract_text.split("\n") if line.strip() != ""]
    assert_lines = []
    non_assert_lines = []
    
    block_keywords = ("for ", "if ", "try", "while ")

    for i, line in enumerate(lines):
        if line.strip().startswith("assert"):
            assert_lines.append((i, line))  # (index, line)
        else:
            non_assert_lines.append((i, line))  # (index, line)
    
    contracts = {}
    for block_idx, (assert_idx, assert_line) in enumerate(assert_lines):
        block_lines = []

        # include non-assert lines that start with block keywords
        for non_assert_idx, non_assert_line in non_assert_lines:
            if non_assert_idx < assert_idx and non_assert_line.strip().startswith(block_keywords):
                block_lines.append(non_assert_line)

        # add assert line
        block_lines.append(assert_line)

        # case1: try only and assert only
        # remove try
        if any(l.strip().startswith("try") for l in block_lines):
            only_assert_inside = all(
                l.strip().startswith("assert") or l.strip().startswith("try")
                for l in block_lines
            )
            if only_assert_inside:
                # remove try and only leave assert
                block_lines = [l for l in block_lines if not l.strip().startswith("try")]

        # fallback: for/if/while block only and no assert → add pass
        fixed_lines = []
        for l in block_lines:
            fixed_lines.append(l)
            if l.strip().startswith(block_keywords) and not any("assert" in bl for bl in block_lines):
                fixed_lines.append("    pass  # auto-fix for empty block")

        contracts[f"assert_{block_idx}"] = "\n".join(fixed_lines)

    return contracts

if __name__ == '__main__':
    random.seed(42) 
    parser = argparse.ArgumentParser()
    parser.add_argument('--models_base_dir', type=str, required=True, help='Base directory of model code files')
    parser.add_argument('--model_names', type=str, required=True, nargs='+', help='List of model names')
    parser.add_argument('--test_cases_json', type=str, required=True, help='Path to test case JSON')
    parser.add_argument('--output_path', type=str, required=True, help='Output directory')
    parser.add_argument('--mode', type=str, required=True, help='Mode')
    args = parser.parse_args()
    output_path = save_path_for_evaluation(args.test_cases_json, args.output_path, args.mode, args.model_names[0])
    # Base Metric Evaluation (Base Metric Evaluation)
    print(f"\n================== Evaluating base metrics ==================")
    #evaluate(args.models_base_dir, args.model_names, args.test_cases_json, args.output_path, args.test_cases_json, args.mode)

    ### Our Metric Evaluation
    print(f"\n================== Evaluating our metrics ==================")
    if 'humaneval' in args.test_cases_json.lower():
        task_funcs = canonical_solution_load_for_reward('humaneval', "in_contracts")
        canon_jsonl = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
    elif 'mbpp' in args.test_cases_json.lower():
        task_funcs = canonical_solution_load_for_reward('mbpp', "in_contracts")
        canon_jsonl = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'

    contracts_map = {}
    with open(canon_jsonl, encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            contract_dict = parse_contracts_by_assert_blocks(rec["contract"])
            contracts_map[rec["task_id"]] = contract_dict
    
    with open(args.test_cases_json, 'r') as f:
        test_json = json.load(f)
        
    evaluator=GrammarRewarder()

    data_total_len = len(contracts_map)
    total_avc = {}
    total_ts = {}
    total_tqs = {}
    
    for task_id, test_case in test_json['test_cases'].items():
        # # Debugging #########################################################
        # if task_id != "HumanEval/76":
        #     continue
        # #####################################################################
        
        if test_case == {}:
            continue
        if task_id not in task_funcs:
            continue
        
        reference_src = task_funcs[task_id][1]
        entry_point = task_funcs[task_id][2]
        parsed_assert_blocks = test_case
        contracts = contracts_map[task_id]
    
        
        reward, detail = evaluator.compute(task_id, reference_src, entry_point, parsed_assert_blocks, contracts)
        
        if detail == {}:
            continue
        
        for key, value in detail.items():
            if key == 'AVC':
                total_avc[task_id] = value
            elif key == 'TS':
                total_ts[task_id] = value
            elif key == 'TQS':
                total_tqs[task_id] = value
            else:
                raise ValueError(f"Unknown key: {key}")
    
    data_total_generation=[]
    data_total_generation_filtered=[]
    for json_task_id in test_json['test_cases'].keys():
        sections = test_json['test_cases'][json_task_id]
        if not isinstance(sections, dict) or not sections:
            continue
        any_non_empty = False
        any_satisfiable = False
        for section, json_dict in sections.items():
            # Count this task only once in total if it has at least one non-empty section
            if isinstance(json_dict, dict):
                if json_dict:
                    any_non_empty = True
                if json_dict.get("is_satisfiable") is True:
                    any_satisfiable = True
            elif isinstance(json_dict, list):
                if len(json_dict) > 0:
                    any_non_empty = True
                    # filtered list implies satisfiable solutions kept
                    any_satisfiable = True
        if any_non_empty:
            data_total_generation.append(json_task_id)
        if any_satisfiable:
            data_total_generation_filtered.append(json_task_id)
            
    print(f"Data_total_generation: {len(set(data_total_generation))}")    
    print(f"Data_total_generation (error filtered): {len(set(data_total_generation_filtered))}")
    
    for total_list, name in [(total_avc, "AVC"), (total_ts, "TS"), (total_tqs, "TQS")]:
        score=0
        if total_list:
            avg_score = sum(total_list.values()) / data_total_len
            print(f"Total {name}: {avg_score}")
        else:
            print(f"Total {name}: N/A (no values)")

    total_dict = {
        "Data_total_len": data_total_len,
        "Data_total_generation": len(set(data_total_generation)),
        "Data_total_generation (error filtered)": len(set(data_total_generation_filtered)),
        "Score": {
            "AVC": sum(total_avc.values()) / data_total_len,
            "TS": sum(total_ts.values()) / data_total_len,
            "TQS": sum(total_tqs.values()) / data_total_len,
        },
        "AVC": total_avc,
        "TS": total_ts,
        "TQS": total_tqs,
    }

    with open(os.path.join(output_path, f"total_results.json"), 'w') as f:
        json.dump(total_dict, f, indent=2)