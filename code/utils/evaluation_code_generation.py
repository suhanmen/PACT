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
import codecs
from typing import Optional, Tuple
import re
import builtins
import codecs
from builtins import set as bset
import signal

sys.set_int_max_str_digits(0)

_docstring_re = re.compile(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', re.DOTALL)

def _strip_triple_quoted(src):
    return _docstring_re.sub('', src)

def safe_eval(input_str, repeat_cap=500_000):
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

def run_func_with_timeout(func, args, timeout=3): 
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
            #return f"{msg[0]}: {msg[2]}"
        
    return "NoResult"

def run_file_with_tests(py_path, test_code): 
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

def run_test_file(file_path, input_args, model_name=None, test_cases_json=None):
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

        result = run_func_with_timeout(func, args_to_pass, timeout=3)
        return result
    
    except AssertionError as e:
        #return f"AssertionError: {e}"
        return f"Exception: {e}"

    except Exception as e:
        return f"Exception: {e}"

### Groundtruth code play
def run_func_object(func, input_args):
    import inspect
    try:
        sig = inspect.signature(func)
        param_count = len(sig.parameters)

        parsed_args = safe_eval(input_args)
        if parsed_args is None:
            return "InvalidInput"

        if param_count == 1:
            if isinstance(parsed_args, (list, tuple)) and len(parsed_args) == 1:
                args_to_pass = [parsed_args[0]]       # unwrap single element
            else:
                args_to_pass = [parsed_args]
        else:
            args_to_pass = parsed_args if isinstance(parsed_args, (list, tuple)) else [parsed_args]
        return run_func_with_timeout(func, args_to_pass, timeout=3)
    
    except AssertionError as e:
        #return f"AssertionError: {e}"
        return f"Exception: {e}"

    except Exception as e:
        return f"Exception: {e}"

### Assert-based testcases
def run_func_with_tests(func, test_code):
    import types
    try:
        env = {'__builtins__': __builtins__}
        if not isinstance(func, types.FunctionType):
            return "InvalidFunction"

        env[func.__name__] = func

        # 5 seconds timeout
        res = run_func_with_timeout(
            lambda c=compile(test_code, "<humaneval_test>", "exec"): exec(c, env), [], timeout=3
        )
        return "Pass" if res is None else res

    except AssertionError as e:
        #return f"AssertionError: {e}"
        return f"Exception: {e}"

    except Exception as e:
        return f"Exception: {e}"

def summarize_results(results, ks=[1, 10, 100], star_for_1=False):
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
    if data_type == "humaneval":
        ds = load_dataset("openai_humaneval", split="test")
        groundtruth_map = {it["task_id"]: it["canonical_solution"] for it in ds}
        output_dir_root = 'Original'
        dataset_tag = "humaneval"
        test_cases = {
            it["task_id"]: [{"test_code": it["test"], "section": "all"}] for it in ds
        }
    elif data_type == "humanevalplus":
        ds = load_dataset("evalplus/humanevalplus", split="test")
        groundtruth_map = {it["task_id"]: it["canonical_solution"] for it in ds}
        output_dir_root = 'Original'
        dataset_tag = "humanevalplus"
        test_cases = {
            it["task_id"]: [{"test_code": it["test"], "section": "all"}] for it in ds
        }
        jsonl_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
        task_funcs = {}
    else:
        with open(test_cases_json, 'r') as f:
           tc_all = json.load(f)
        test_cases_model_name = list(tc_all.keys())[0]
        test_cases = list(tc_all.values())[0] if isinstance(tc_all, dict) and len(tc_all) == 1 else tc_all
        groundtruth_map = None
        
        if 'gpt_outputs' in test_cases_json:
            output_dir_root = test_cases_json.split('/')[7]
        else:
            output_dir_root = test_cases_json.split('/')[6]
        dataset_tag = os.path.splitext(os.path.basename(test_cases_json))[0]

    return output_dir_root, test_cases, dataset_tag, test_cases_model_name 
    
def _inject_contracts_into_solution(sol, contracts, entry):
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

def has_no_tests(block):
    def extract_section(header: str):
        pattern = rf"{header}:[ \t]*\n([^\n]*)"
        matches = re.findall(pattern, block, flags=re.I)
        return matches[-1].strip() if matches else None

    func_val = extract_section("Functionality Test Cases")
    contract_val = extract_section("Contract Test Cases")

    func_none = func_val is not None and func_val.lower() == "none"
    contract_none = contract_val is not None and contract_val.lower() == "none"
    return func_none, contract_none

def generated_solution_load(output_path, mode, test_case_model_name, code_generation_model_name):
    model_tag={
        "DeepSeek": "DeepSeek-R1-Distill-Qwen-14B",
    }

    if 'humaneval' in output_path:
        jsonl_path = f'../../code/output_base/humaneval/inference/{mode}/{model_tag[code_generation_model_name]}/generated_step_all.json'
        answer_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
    elif 'mbpp' in output_path:
        jsonl_path = f'../../code/output_base/mbpp/inference/{mode}/{model_tag[code_generation_model_name]}/generated_step_all.json'
        answer_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
        
    task_funcs = {}
    answer_lines = []
    None_ist = []

    with open(jsonl_path, 'r', encoding='utf-8') as f:
        generated_lines = json.load(f)
        generated_lines = generated_lines['DeepSeek-R1-Distill-Qwen-14B']
    with open(answer_path, 'r', encoding='utf-8') as f:
        for line in f:
            answer_lines.append(json.loads(line))
    
    for generated,answer in zip(generated_lines, answer_lines):
        try:            
            if mode == "make_code_block_ft_ct":
                func_none, contract_none = has_no_tests(generated['input'])
                if func_none or contract_none:
                    None_ist.append(generated['task_id'][0])
            elif mode == "code_refinement_with_instructions_fc_ct":
                if generated['input'] == 'None':
                    None_ist.append(generated['task_id'][0])
            
            generated_solution = generated['parsed_outputs']['code']
            
        except Exception as e:
            print(f"❌ [{generated['task_id'][0]}] Code not parsed with an error: {e}")
            continue


        entry_point = answer['entry_point']
        task_id = answer['task_id']
        #prompt = answer['prompt']
        #contract = answer['contract']
        #canonical_solution = answer['canonical_solution']
        full_code = generated_solution

        local_env = {}
        if task_id == 'Mbpp/260' and mode == 'make_code_block_fs_cs':
            continue
        try:
            exec(textwrap.dedent(full_code), local_env)  
            if entry_point not in local_env:
                print(f" {task_id}: '{entry_point}' not found in executed code")
                continue

            task_funcs[task_id] = local_env[entry_point]  
        except Exception as e:
            print(f"❌ [{task_id}] Code execution error: {e}")
            continue
    return task_funcs, None_ist


def str_func_to_func_obj(str_func: str, entry_point: str, gt_source: str = None):
    local_env = {}
    
    if gt_source:
        try:
            mod = ast.parse(gt_source)
            new_body = []
            for node in mod.body:
                if isinstance(node, ast.FunctionDef) and node.name == entry_point:
                    continue
                new_body.append(node)
            mod.body = new_body
            cleaned_source = ast.unparse(mod)
            exec(cleaned_source, local_env)
        except Exception as e:
            print(f"⚠️ GT source cleanup failed: {e}")

    exec(str_func, local_env)
    return local_env[entry_point]


def canonical_solution_load_for_reward(dataset_tag, contracts_in="no_contracts"):
    """
    return: { task_id: (func_obj, source_str) }
    """

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

            try:
                func_obj = str_func_to_func_obj(clean_code, entry_point)
                task_map[task_id] = (func_obj, clean_code, entry_point)
            except Exception as e:
                print(f"[skip] {task_id}: {e}")
    return task_map

def is_assert_case(r):
    return isinstance(r['groundtruth_result'], str) and r['groundtruth_result'].startswith("Assert")

def collapse_case_runs(case_runs_dict):
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

def _encode_json_friendly(o):
    if isinstance(o, (bytes, bytearray, memoryview)):
        try:
            return o.decode("utf-8")                 
        except UnicodeDecodeError:
            return base64.b64encode(o).decode("ascii") 

    if isinstance(o, set):
        return list(o)

    if isinstance(o, complex):
        return [o.real, o.imag]

    raise TypeError(f"{type(o).__name__} is not JSON serializable")

def make_json_serializable(obj):
    if obj is ...:
        return None   
    if isinstance(obj, dict):
        return {str(k): make_json_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple, set)):
        return [make_json_serializable(v) for v in obj]
    elif isinstance(obj, np.generic):
        return obj.item()
    elif isinstance(obj, complex):
        return {"real": obj.real, "imag": obj.imag}
    else:
        return obj

def extract_python_code(md):
    pattern = r'```python\s*(.*?)```'
    blocks = re.findall(pattern, md, re.DOTALL)
    return '\n\n'.join(block.strip() for block in blocks)

# =========================
# Reward helper functions
# =========================

def _load_plus_inputs_for_task(dataset_tag: str, task_id: str):
    """Load base inputs (Plus dataset) for a given task_id.
    dataset_tag must contain 'humaneval' or 'mbpp'.
    Returns a list of inputs (each item is a string or JSON-serializable) or [].
    """
    if 'humaneval' in dataset_tag.lower():
        jsonl_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
    elif 'mbpp' in dataset_tag.lower():
        jsonl_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
    else:
        return []

    try:
        with open(jsonl_path, 'r', encoding='utf-8') as f:
            for line in f:
                rec = json.loads(line)
                if rec.get('task_id') == task_id:
                    # Both datasets store base inputs under 'plus_input'
                    return rec.get('plus_input', []) or []
    except Exception:
        return []
    return []

def _run_func_object_maybe_dict(func, input_args, contract_test_case_type: str):
    """Run function with input that may be a dict (param-name keyed) or a literal string.
    - If input_args is a dict: map by parameter names order.
    - Else: reuse run_func_with_timeout with parsed args via safe_eval.
    Returns the raw result from run_func_with_timeout: normal value or string like 'AssertionError: ...' or 'Exception: ...' etc.
    """
    sig = inspect.signature(func)
    param_count = len(sig.parameters)

    # grammar input
    if isinstance(input_args, dict) and contract_test_case_type == "grammar":
        param_names = list(sig.parameters.keys())
        if param_count == 1:
            if param_names[0] in input_args:
                args_to_pass = [input_args[param_names[0]]]
            else:
                return "InvalidInput"
        else:
            args_to_pass = []
            for name in param_names:
                if name in input_args:
                    args_to_pass.append(input_args[name])
                else:
                    return "InvalidInput"
        return run_func_with_timeout(func, args_to_pass, timeout=3)
    
    # direct input
    elif contract_test_case_type == "direct":
        # Fallback to string/literal inputs
        parsed_args = safe_eval(input_args)
        if parsed_args is None:
            return "InvalidInput"
        if param_count == 1:
            if isinstance(parsed_args, (list, tuple)) and len(parsed_args) == 1:
                args_to_pass = [parsed_args[0]]
            else:
                args_to_pass = [parsed_args]
        else:
            args_to_pass = parsed_args if isinstance(parsed_args, (list, tuple)) else [parsed_args]
        return run_func_with_timeout(func, args_to_pass, timeout=3)

def compute_functionality_score(task_id: str, generated_func_str, functionality_dataset, dataset_tag: str) -> float:
    """Compute functionality score using original Plus base inputs.
    - Loads GT function (no contracts) via canonical_solution_load_for_reward.
    - Compares generated_func outputs with GT on each base input.
    Returns success ratio in [0.0, 1.0].
    """
    # Parameters
    generated_func_dict={}
    
    gt_map = canonical_solution_load_for_reward(dataset_tag, contracts_in="no_contracts")

    if isinstance(generated_func_str, str):
        try:
            generated_obj = str_func_to_func_obj(generated_func_str, gt_map[task_id][2], gt_map[task_id][1])
            generated_func_dict[task_id] = (generated_obj, generated_func_str, gt_map[task_id][2])
            generated_func = generated_obj
        except Exception as e:
            print(f"❌ [{task_id}] Code execution error: {e}")
            return 0.0
    
    if task_id not in gt_map:
        return 0.0
    
    gt_func = gt_map[task_id][0]
    
    if isinstance(functionality_dataset, dict):
        if functionality_dataset["task_id"] == task_id:
            inputs = functionality_dataset["plus_input"] # plus_input
            #*** for RL
            # random.seed(42)
            # all_inputs = functionality_dataset["plus_input"]
            # total_inputs = len(all_inputs)
            # test_size = int(total_inputs * 0.8) 
            # shuffled_inputs = random.sample(all_inputs, total_inputs)
            # inputs = shuffled_inputs[:test_size]
        else:
            return 0.0
    else:
        inputs = _load_plus_inputs_for_task(functionality_dataset, task_id)
    
    if not inputs:
        return 0.0

    total = 0
    passed = 0
    for inp in inputs:
        total += 1
        gt_res = run_func_object(gt_func, inp)
        model_res = run_func_object(generated_func, inp)

        is_err_model = isinstance(model_res, str) and (re.match(r'^(?:[A-Za-z_]\w*Error|Exception):', model_res) or model_res in ("Timeout", "InvalidInput"))
        is_err_gt    = isinstance(gt_res, str) and (re.match(r'^(?:[A-Za-z_]\w*Error|Exception):', gt_res) or gt_res in ("Timeout", "InvalidInput"))
        if is_err_model and is_err_gt:
            succ = True
        else:
            succ = (model_res == gt_res)
        if succ:
            passed += 1

    return (passed / total) if total > 0 else 0.0


def compute_contracts_score(task_id: str, generated_func_str, contract_test_cases, dataset_tag: str, contract_test_case_type: str) -> float:
    """Compute contracts score using Grammar-SMT test cases JSON.
    - Counts proportion of violated solutions that trigger AssertionError in generated_func.
    The JSON structure must be the one produced by grammar SMT (see evaluation_test_case_pass_k_for_grammar.py).
    """
    
    task_group = contract_test_cases
        
    # change str -> func_obj
    gt_map = canonical_solution_load_for_reward(dataset_tag, contracts_in="in_contracts")
        
    if isinstance(generated_func_str, str):
        try:
            generated_func_dict={}
            generated_obj = str_func_to_func_obj(generated_func_str, gt_map[task_id][2], gt_map[task_id][1])
            generated_func_dict[task_id] = (generated_obj, generated_func_str, gt_map[task_id][2])
            generated_func = generated_func_dict[task_id][0]
        except Exception as e:
            return 0.0
        
    total = 0
    passed = 0

    
    for section, cases in task_group.items():
        
        if contract_test_case_type == "grammar":
            # Only check violated sections; skip if nothing after 'violated_'
            try:
                if section.split('violated_')[1] == '':
                    continue
            except Exception:
                # If section naming not following convention, treat as generic violated section
                pass


        try:
            solutions = cases.get(task_id, []) if isinstance(cases, dict) else []
        except Exception:
            print(f"❌ Data format error: {section}")
            pdb.set_trace()
        
        for sol in solutions:
            inp = sol.get('input')

            # Only keep cases where GT contracts actually assert
            gt_res = _run_func_object_maybe_dict(gt_map[task_id][0], inp, contract_test_case_type)
            gt_assert = isinstance(gt_res, str) and (gt_res.startswith('AssertionError') or ('AssertionError' in gt_res))
            if not gt_assert:
                continue
            
            total += 1
            res = _run_func_object_maybe_dict(generated_func, inp, contract_test_case_type)
            
            # Success when an AssertionError is triggered by generated code
            ok = isinstance(res, str) and (res.startswith('AssertionError') or ('AssertionError' in res))
            if ok:
                passed += 1
    return (passed / total) if total > 0 else 0.0


def compute_contracts_score_gt(task_id: str, grammar_test_cases_json, dataset_tag: str, contract_test_case_type: str) -> float:
    """Compute contracts score for the GT (canonical) function using Grammar-SMT test cases JSON."""
    try:
        gt_map = canonical_solution_load_for_reward(dataset_tag, contracts_in="in_contracts")
        if task_id not in gt_map:
            return 0.0
        gt_func = gt_map[task_id][0]
    except Exception:
        return 0.0

    # Use the pre-filtered contracts_dataset directly
    if isinstance(grammar_test_cases_json, dict):
        task_group = grammar_test_cases_json


    total = 0
    passed = 0

    for section, cases in task_group.items():
        if isinstance(cases, dict) and cases is False:
            continue
        try:
            if section.split('violated_')[1] == '':
                continue
        except Exception:
            pass
        
        # Access the correct data structure
        solutions = cases.get(task_id, []) if isinstance(cases, dict) else []
        
        for sol in solutions:
            inp = sol.get('input')
            total += 1
            res = _run_func_object_maybe_dict(gt_func, inp, contract_test_case_type)
            ok = isinstance(res, str) and (res.startswith('AssertionError') or ('AssertionError' in res))
            if ok:
                passed += 1

    return (passed / total) if total > 0 else 0.0


def compute_string_contract_metrics(functionality_dataset, generated_func_str):
    # Use AST-based extraction; compare only test expressions (ignore messages)
    contract_src = functionality_dataset.get('contract', '') or ''
    entry_point = functionality_dataset.get('entry_point')

    # 1) GT: contracts text may be module-level asserts
    gt_asserts_all, gt_asserts_module = extract_asserts_flattened(contract_src, entry_point=None)

    # 2) GEN: restrict to entry_point function body if available
    gen_asserts_all, gen_asserts_module = extract_asserts_flattened(generated_func_str, entry_point=entry_point)

    
    # 3) Normalize both sides to comparable strings
    gt_norm = [normalize(a) for a in gt_asserts_module]
    gen_norm = [normalize(a) for a in gen_asserts_module]

    matched = builtins.set(gt_norm) & builtins.set(gen_norm)

    aar = len(matched) / len(gt_norm) if gt_norm else 0.0
    aap = len(matched) / len(gen_norm) if gen_norm else 0.0


    unmatched_gt = sorted(list(bset(gt_norm) - matched))
    unmatched_generated = sorted(list(bset(gen_norm) - matched))
    
    details = {
        "gt_contracts": sorted(gt_asserts_all),
        "gen_contracts": sorted(gen_asserts_all),
        "matched": sorted(list(matched)),
        "unmatched_gt": unmatched_gt,
        "unmatched_generated": unmatched_generated,
        "gt_total": len(gt_norm),
        "gen_total": len(gen_norm),
    }
    return aar, aap, details

# --- Helpers for AST-based extraction/normalization ---

def _flatten_bool_and(expr: ast.AST) -> list:
    """Flatten a boolean expression joined by 'and' into a list of sub-expressions.
    If not an 'and'-joined BoolOp, return [expr].
    """
    if isinstance(expr, ast.BoolOp) and isinstance(expr.op, ast.And):
        items = []
        for v in expr.values:
            items.extend(_flatten_bool_and(v))
        return items
    return [expr]


def _normalize_all_any_call(expr: ast.AST) -> ast.AST:
    """Normalize all()/any() calls so that list comprehension and generator
    expressions are treated equivalently.
    E.g., all([cond for x in xs]) -> all(cond for x in xs)
    """
    class Rewriter(ast.NodeTransformer):
        def visit_Call(self, node: ast.Call):
            self.generic_visit(node)
            # Expect simple form: all(<one-arg>) or any(<one-arg>)
            func_id = None
            if isinstance(node.func, ast.Name):
                func_id = node.func.id
            if func_id in {"all", "any"} and len(node.args) == 1 and not node.keywords:
                arg = node.args[0]
                # Convert ListComp to GeneratorExp
                if isinstance(arg, ast.ListComp):
                    gen = ast.GeneratorExp(elt=arg.elt, generators=arg.generators)
                    node.args[0] = gen
            return node
    try:
        mod = ast.fix_missing_locations(Rewriter().visit(ast.parse(ast.unparse(expr))))
        # Re-parse and extract the normalized expr back
        if isinstance(mod, ast.Module) and mod.body and isinstance(mod.body[0], ast.Expr):
            return mod.body[0].value
    except Exception:
        pass
    return expr


def _normalize_assert_str_from_test_msg(test_expr: ast.AST, msg_expr: Optional[ast.AST]) -> str:
    # Normalize all()/any() forms in test expression
    test_expr = _normalize_all_any_call(test_expr)

    try:
        test_str = ast.unparse(test_expr).strip()
    except Exception:
        try:
            import astor
            test_str = astor.to_source(test_expr).strip()
        except Exception:
            test_str = ""
    if msg_expr is not None:
        try:
            msg_str = ast.unparse(msg_expr).strip()
        except Exception:
            try:
                import astor
                msg_str = astor.to_source(msg_expr).strip()
            except Exception:
                msg_str = None
    else:
        msg_str = None
    return f"assert {test_str}, {msg_str}" if msg_str else f"assert {test_str}"

def _normalize_assert_str(test_expr: ast.AST) -> list:
    # Normalize all()/any() forms in test expression
    test_expr = _normalize_all_any_call(test_expr)
    try:
        test_str = ast.unparse(test_expr).strip()
    except Exception:
        try:
            import astor
            test_str = astor.to_source(test_expr).strip()
        except Exception:
            test_str = ""
    return f"assert {test_str}"

def extract_asserts_flattened(src: str, entry_point: Optional[str] = None) -> tuple[list, list]:
    """Extract assert statements as normalized strings, splitting on 'and'.
    - If entry_point is provided, only considers asserts inside that function.
    - Comments are ignored (AST based).
    - Compound asserts like `assert A and B, msg` become two: `assert A, msg` and `assert B, msg`.
    """
    if not isinstance(src, str) or not src.strip():
        return [], []

    # If fenced code blocks exist, extract python code first
    src_candidate = extract_python_code(src) if '```' in src else src
    # Try parsing the whole block first
    try:
        mod = ast.parse(src_candidate)
    except Exception:
        # Fallback: per-line assert parsing (handles bullets or extra text)
        collected_all = []
        collected_module = []
        for raw in src_candidate.splitlines():
            line = raw.strip()
            if not line:
                continue
            # remove list bullets like '- ' or '* '
            if line.startswith('- '):
                line = line[2:].lstrip()
            elif line.startswith('* '):
                line = line[2:].lstrip()
            # consider only lines starting with 'assert'
            if not line.startswith('assert'):
                continue
            try:
                node = ast.parse(line)
                if node.body and isinstance(node.body[0], ast.Assert):
                    a = node.body[0]
                    for part in _flatten_bool_and(a.test):
                        s1 = _normalize_assert_str_from_test_msg(part, a.msg)
                        s2 = _normalize_assert_str(part)
                        if s1:
                            collected_all.append(s1)
                        if s2:
                            collected_module.append(s2)
            except Exception:
                continue
        return collected_all, collected_module
    
    # Full-module path
    class Collector(ast.NodeVisitor):
        def __init__(self, target: Optional[str]):
            self.target = target
            self.in_target = target is None
            self.collected: list[str] = []
            self.collected_tests: list[str] = []
        
        def visit_FunctionDef(self, node: ast.FunctionDef):
            prev = self.in_target
            if self.target is None or node.name == self.target:
                self.in_target = True
                self.generic_visit(node)
                self.in_target = prev
            else:
                self.generic_visit(node)
        
        def visit_Assert(self, node: ast.Assert):
            if not self.in_target:
                return
            parts = _flatten_bool_and(node.test)
            for p in parts:
                s1 = _normalize_assert_str_from_test_msg(p, node.msg)
                s2 = _normalize_assert_str(p)
                if s1:
                    self.collected.append(s1)
                if s2:
                    self.collected_tests.append(s2)

    c = Collector(entry_point)
    c.visit(mod)

    if c.collected:
        return c.collected, c.collected_tests

    # Secondary fallback: regex-scan lines containing 'assert' even if module parsed but no asserts collected
    collected = []
    collected_tests = []
    for raw in src_candidate.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith('- '):
            line = line[2:].lstrip()
        elif line.startswith('* '):
            line = line[2:].lstrip()
        if 'assert' not in line:
            continue
        # try to find an 'assert' starting segment within the line
        m = re.search(r'(assert\s+.*)$', line)
        if not m:
            continue
        snippet = m.group(1)
        try:
            node = ast.parse(snippet)
            if node.body and isinstance(node.body[0], ast.Assert):
                a = node.body[0]
                for part in _flatten_bool_and(a.test):
                    s = _normalize_assert_str_from_test_msg(part, a.msg)
                    if s:
                        collected.append(s)
                    s2 = _normalize_assert_str(part)
                    if s2:
                        collected_tests.append(s2)
        except Exception:
            continue
    return collected, collected_tests


def normalize(s: str) -> str:
    # unify quotes, spaces, and minor tokens
    s = s.replace('"', "'")
    # common aliasing
    s = s.replace("inputs", "input")
    # remove redundant outer spaces
    s = re.sub(r"\s+", " ", s)
    # remove redundant parentheses around generator in all/any
    s = re.sub(r"all\s*\(\s*\((.*)\)\s*\)", r"all(\1)", s)
    s = re.sub(r"any\s*\(\s*\((.*)\)\s*\)", r"any(\1)", s)
    return s.strip()


def extract_asserts_from_code(code_str: str):
    """Backward-compatible wrapper: full asserts as strings (not split).
    Prefer using extract_asserts_flattened for matching.
    """
    try:
        mod = ast.parse(code_str)
    except SyntaxError:
        return []
    out = []
    for node in ast.walk(mod):
        if isinstance(node, ast.Assert):
            try:
                out.append(ast.unparse(node).strip())
            except Exception:
                try:
                    import astor
                    out.append(astor.to_source(node).strip())
                except Exception:
                    pass
    return out

class EvaluationRewarder:
    """Original/Grammar """
    def __init__(self, humaneval_functionality_dataset_path, mbpp_functionality_dataset_path, humaneval_contracts_dataset_path, mbpp_contracts_dataset_path, contract_test_case_type):
        self.humaneval_functionality_dataset_path = humaneval_functionality_dataset_path
        self.mbpp_functionality_dataset_path = mbpp_functionality_dataset_path
        self.humaneval_contracts_dataset_path = humaneval_contracts_dataset_path
        self.mbpp_contracts_dataset_path = mbpp_contracts_dataset_path
        self.contract_test_case_type = contract_test_case_type
        
        # functionality dataset
        functionality_data_dict={}
        for dataset_path in [self.humaneval_functionality_dataset_path, self.mbpp_functionality_dataset_path]:
            with open(dataset_path, 'r', encoding='utf-8') as f:
                dataset = [json.loads(line) for line in f if line]
                for i in dataset:
                    functionality_data_dict[i['task_id']] = i
        
        self.functionality_dataset = functionality_data_dict
        

        contract_data_dict={}
        for dataset_path in [self.humaneval_contracts_dataset_path, self.mbpp_contracts_dataset_path]:
            # contract_data_dict[dataset_name] = {}
            # with open(dataset_path, 'r', encoding='utf-8') as f:
            #     dataset = [json.loads(line) for line in f if line]
            #     for i in dataset:
            #         contract_data_dict[dataset_name][i['task_id']] = i        
            # contracts dataset
            with open(dataset_path, 'r') as f:
                contract_dataset=json.load(f)
                task_id_list = []
                
                for i in contract_dataset:
                    task_id_list.append(i['task_id'])
                
                task_id_list = sorted(list(set(task_id_list)), key=lambda x: int(x.split('/')[1]))
                
                
                for i in task_id_list:
                    contract_data_dict[i] = {}
                    for k in contract_dataset:
                        if k["task_id"] == i:
                            if k['section'] not in contract_data_dict[i]:
                                contract_data_dict[i][k['section']] = {i:[]}
                            try:
                                if k['groundtruth_result'].startswith('AssertionError'):
                                    contract_data_dict[i][k['section']][i].append({'input':k['input']})
                            except:
                                pass
                            
        self.contracts_dataset = contract_data_dict
        
    def python_like_to_json(self,text):
        text = text.replace("True", "true").replace("False", "false").replace("None", "null")
        #text = re.sub(r"\(([^()]*?,[^()]*?)\)", r"[\1]", text)
        return text
    
    def python_like_to_python(self,text):
        text = text.replace("true", "True").replace("false", "False").replace("null", "None")
        return text

    
    def extract_code_block(self,text):
        if isinstance(text, list):
            if not text:
                return None
            text = text[0]
        
        # Try triple quotes pattern first - handle multiline with flexible whitespace
        match = re.search(r'"code":\s*\'\'\'(.*?)\'\'\'', text, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        # Try triple quotes pattern with newlines and spaces
        match = re.search(r'"code":\s*\'{3}([\s\S]*?)\'{3}', chosen, re.DOTALL)
        if match:
            return match.group(1).strip()

        
        # Try double quotes pattern for JSON 
        match = re.search(r'"code":\s*"([^"]*(?:\\.[^"]*)*)"', text, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        return None
    
    

    def parsing_code_generation_func(self, code_generation_model_path, model_inference: str, entry_point: str = None):
        """
        Robust parser for model_inference:
        - Prefer content AFTER the last </think> tag
        - Collect ALL fenced code blocks in that tail first
        - Prefer the one containing the entry_point function
        - If none found, fallback to JSON-in-text in the tail
        - Otherwise fallback to scanning the entire text (legacy behavior)
        """
        
        def timeout_handler(signum, frame):
            raise TimeoutError("Parsing timeout after 4 seconds")

        def _extract_from_text(txt: str) -> Optional[str]:
            blocks = re.findall(r"```[a-zA-Z]*\s*([\s\S]*?)```", txt, re.DOTALL)
            if blocks:

                chosen = None
                if entry_point:
                    for b in blocks:
                        if f"def {entry_point}" in b or '"code"' in b:
                            chosen = b
                            break
                if not chosen:
                    chosen = blocks[-1]


                if '{' in chosen and '"code"' in chosen:
                    m = re.search(r'"code":\s*\'{3}([\s\S]*?)\'{3}', chosen, re.DOTALL)
                    if m:
                        return m.group(1).strip()

                    m = re.search(r'"code":\s*"([^"]*(?:\\.[^"]*)*)"', chosen, re.DOTALL)
                    if m:
                        return codecs.decode(m.group(1), "unicode_escape").strip()

                    m = re.search(r'(?s)(?:from\s+[^\n]+\n|import\s+[^\n]+\n|#.*\n|\s*\n)*def\s+\w+\s*\([^)]*\):.*', chosen)
                    if m:
                        return m.group(0).strip()

                m = re.search(r'(?s)(?:from\s+[^\n]+\n|import\s+[^\n]+\n|#.*\n|\s*\n)*def\s+\w+\s*\([^)]*\):.*', chosen)
                if m:
                    return m.group(0).strip()
                return chosen.strip()

            m = re.search(r'"code":\s*\'{3}([\s\S]*?)\'{3}', txt, re.DOTALL)
            if m:
                return m.group(1).strip()

            m = re.search(r'(?s)(?:from\s+[^\n]+\n|import\s+[^\n]+\n|#.*\n|\s*\n)*def\s+\w+\s*\([^)]*\):.*', txt)
            if m:
                return m.group(0).strip()

            m = re.search(r"\{[\s\S]*?\}\s*$", txt)
            if m:
                blob = m.group(0).strip()
                # Try strict JSON first
                try:
                    obj = json.loads(blob)
                    if isinstance(obj, dict) and 'code' in obj and isinstance(obj['code'], str):
                        return obj['code'].strip("\n")
                except Exception:
                    pass
                # Fallback to extractor with improved handling
                try:
                    # Handle triple quotes in JSON strings
                    json_blob = re.sub(r'"code":\s*\'{3}(.*?)\'{3}', 
                                     lambda m: f'"code": {json.dumps(m.group(1))}', 
                                     blob, flags=re.DOTALL)
                    
                    json_blob = self.python_like_to_json(json_blob)
                    code_str = self.extract_code_block(json_blob)
                    if code_str:
                        return codecs.decode(code_str, "unicode_escape").strip("\n")
                except Exception:
                    pass
            return None

        def _finalize_code(s: Optional[str]) -> Optional[str]:
            if not isinstance(s, str):
                return s
            out = s.strip()

            # remove the fence
            out = re.split(r"\n```.*$", out, maxsplit=1)[0]
            lines = out.rstrip().splitlines()
            if lines and lines[-1].strip() == "}":
                out = "\n".join(lines[:-1])

            # remove the last quote
            if out.endswith('"') or out.endswith("'"):
                if not ((out.startswith('"') and out.endswith('"')) or (out.startswith("'") and out.endswith("'"))):
                    out = out[:-1]

            if (out.startswith('"') and out.endswith('"')) or (out.startswith("'") and out.endswith("'")):
                try:
                    out = codecs.decode(out[1:-1], "unicode_escape")
                except Exception:
                    out = out[1:-1]

            try:
                out = codecs.decode(out, "unicode_escape")
            except Exception:
                pass

            return out.strip()

        def _postprocess_code(s: Optional[str]) -> Optional[str]:
            if not isinstance(s, str):
                return s
            out = s.strip()
            # Strip surrounding quotes if present and unescape common sequences
            if (out.startswith('"') and out.endswith('"')) or (out.startswith("'") and out.endswith("'")):
                out = out[1:-1]
                try:
                    out = codecs.decode(out, "unicode_escape")
                except Exception:
                    pass
            return out.strip("\n")
        
        # Set up timeout handler
        old_handler = signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(2)  # 4 seconds timeout
        
        try:
            # Prefer tail after last </think> #########################################################
            tail_idx = model_inference.rfind("</think>")
            if tail_idx != -1:
                tail = model_inference[tail_idx + len("</think>"):]
                got = _extract_from_text(tail)
                
                if got:
                    signal.alarm(0)  # Cancel timeout
                    signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
                    return got
                else:
                    got = _postprocess_code(tail)
                    if got and not "```json" in got and not "code" in got:
                        signal.alarm(0)  # Cancel timeout
                        signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
                        return got
            
            else:
                # Check if the entire text is a function definition
                txt = model_inference.strip()
                
                # Check if it starts with 'def ' and contains a complete function
                if txt.startswith('def '):
                    # Try to find the complete function by looking for proper indentation
                    lines = txt.split('\n')
                    if len(lines) >= 2:  # At least function signature + body
                        # Check if it's a complete function (ends with return statement or has proper structure)
                        if any('return' in line for line in lines) or len(lines) > 2:
                            signal.alarm(0)  # Cancel timeout
                            signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
                            return txt
                
                # Check if it contains import statements followed by a function definition
                if 'from ' in txt and 'import ' in txt and 'def ' in txt:
                    # Extract the function definition part
                    def_pattern = r'def\s+\w+\s*\([^)]*\):.*?(?=\n\ndef|\n\nclass|\n\n$|\Z)'
                    match = re.search(def_pattern, txt, re.DOTALL)
                    if match:
                        # Include import statements + function definition
                        import_lines = []
                        lines = txt.split('\n')
                        for line in lines:
                            if line.strip().startswith(('from ', 'import ')) or not line.strip():
                                import_lines.append(line)
                            else:
                                break
                        
                        # Combine import lines with function definition
                        import_part = '\n'.join(import_lines).strip()
                        if import_part:
                            signal.alarm(0)  # Cancel timeout
                            signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
                            return import_part + '\n\n' + match.group(0).strip()
                        else:
                            signal.alarm(0)  # Cancel timeout
                            signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
                            return match.group(0).strip()
                
                # Also check for function definitions that might be embedded in other text
                def_pattern = r'def\s+\w+\s*\([^)]*\):.*?(?=\n\ndef|\n\nclass|\n\n$|\Z)'
                match = re.search(def_pattern, txt, re.DOTALL)
                if match:
                    if '```' in match.group(0):
                        result = _finalize_code(match.group(0).strip())
                        signal.alarm(0)  # Cancel timeout
                        signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
                        return result
                    else:
                        signal.alarm(0)  # Cancel timeout
                        signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
                        return match.group(0).strip()
                
            # Legacy fallback over entire text
            got = _extract_from_text(model_inference)
            if got is None:
                got = model_inference
            
            signal.alarm(0)  # Cancel timeout
            signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
            return got
            
        except TimeoutError:
            signal.alarm(0)  # Cancel timeout
            signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
            print(f"⚠️ Parsing timeout for task_id: {getattr(self, 'current_task_id', 'unknown')}")
            return None
        except Exception as e:
            signal.alarm(0)  # Cancel timeout
            signal.signal(signal.SIGALRM, old_handler)  # Restore old handler
            print(f"⚠️ Parsing error: {e}")
            return None



    def _check_functionality(self, task_id, generated_func, functionality_test_cases):
        """GT(no_contracts) use base input for functionality reward"""
        return compute_functionality_score(task_id, generated_func, functionality_test_cases, task_id.split("/")[0].lower())

    def _check_contracts(self, task_id, generated_func, contracts_test_cases):
        """Grammar SMT JSON's violated cases for contracts score calculation"""
        return compute_contracts_score(task_id, generated_func, contracts_test_cases, task_id.split("/")[0].lower(), self.contract_test_case_type)
    
    def reward(self, code_generation_model_path, task_id, model_inference):
        print(task_id)
        

        # if "Llama-3.1-8B-Instruct/code_generation_ct" in code_generation_model_path and task_id == "HumanEval/100":
        #     return 0, 0, 0, 0, 0, None, None
        # elif "Phi-4-reasoning-plus/code_generation_ct" in code_generation_model_path and task_id == "HumanEval/163":
        #     return 0, 0, 0, 0, 0, None, Noneㅂ
        # elif "Phi-4-reasoning-plus/code_generation_ct-gh" in code_generation_model_path and task_id == "HumanEval/163":
        #     return 0, 0, 0, 0, 0, None, None
        # elif "Phi-4-reasoning/code_generation_ct" in code_generation_model_path and task_id == "HumanEval/163":
        #     return 0, 0, 0, 0, 0, None, None


        original=model_inference
        generated_func = self.parsing_code_generation_func(code_generation_model_path,model_inference)

        if generated_func is None:
            print("X generated_func is None")
            return 0.0, 0.0, 0.0, 0.0, 0.0, None, None
        
        generated_func = self.python_like_to_python(generated_func)
        
        # functionality reward
        functionality_reward = self._check_functionality(task_id, generated_func, self.functionality_dataset[task_id])
        
        # contracts reward (generated)
        try:
            contracts_reward = self._check_contracts(task_id, generated_func, self.contracts_dataset[task_id])
        except Exception:
            contracts_reward = 0.0
        
        # contracts reward (GT)
        try:
            gt_contracts_check = compute_contracts_score_gt(task_id, self.contracts_dataset[task_id], task_id.split("/")[0].lower(), self.contract_test_case_type)
        except Exception:
            gt_contracts_check = 0.0
        
        # Assertion alignment metrics (AAR/AAP)
        
        if generated_func:
            aar, aap, align_details = compute_string_contract_metrics(self.functionality_dataset[task_id], generated_func)
        else:
            aar, aap, align_details = 0.0, 0.0, []

        total_reward = 0.25*functionality_reward + 0.25*contracts_reward + 0.25*aar + 0.25*aap
        
        details = {
            "gt_contracts_check": gt_contracts_check,
            "functionality_reward": functionality_reward,
            "contracts_reward": contracts_reward,
            "AAR": aar,
            "AAP": aap,
            "alignment_details": align_details,
        }

        return functionality_reward, contracts_reward, aar, aap, total_reward, details, generated_func

    def evaluate(self):
        """keep the same evaluate function as before"""
        return evaluate(
            self.models_base_dir,
            self.test_case_model_names,
            self.code_generation_model_name,
            self.test_cases_json,
            self.output_path,
            # keep the same behavior as before
            self.data_type,
            self.mode,
            self.use_None_list,
        )

def evaluate(models_base_dir, test_case_model_name, code_generation_model_name,test_cases_json, output_path, data_type, mode, use_None_list=False):
    output_dir_root, test_cases, dataset_tag, test_cases_model_name = test_case_load(test_cases_json, data_type)
    canonical_solution_code = canonical_solution_load(output_path, 'in_contracts')
    canonical_solution_code_no_contracts = canonical_solution_load(output_path, 'no_contracts')
    
    dataset_tag = dataset_tag.split("_pre_filtering_results_filtered")[0]
    
    
    if 'code_generation' in mode:
        generated_solution_code, None_list = generated_solution_load(output_path, mode, test_case_model_name, code_generation_model_name)
    
    assert_fail_len = 0
    for model_name in test_case_model_name:
        results = []    
        print(f"=== Evaluating Model: {model_name} ===")
        print(f"=== Which Testcase: {test_cases_json} ===")
        
        model_out = os.path.join(output_path, f"{mode}_in_task_id", output_dir_root, code_generation_model_name) # Save root

        print(f"Output path: {model_out}")
        os.makedirs(model_out, exist_ok=True)
        
        temp = 0.0
        MAX_K = 1 if temp == 0.0 else 100     
        per_task_runs = defaultdict(list)      
        per_task_runs_contract = defaultdict(list)  
        per_task_runs_func     = defaultdict(list)

        for run_idx in range(MAX_K):
            print(f"▶ Run {run_idx + 1}/{MAX_K}")
            for task_id, raw in tqdm(test_cases.items(), desc=f"[{model_name}] Tasks", leave=False):
            
                if use_None_list and task_id in None_list:
                    continue
                
                if isinstance(raw, list):
                    grouped = defaultdict(list)
                    for case in raw:
                        grouped[case.get('section', 'all')].append(case)
                else:
                    grouped = raw
                
                if model_name == 'ground_truth':
                    model_py = 'ground_truth'

                task_success = True  # Whether this task is completely passed in this run
                
                for section, cases in grouped.items():
                    for idx, case in enumerate(cases, start=1):
                        # (A) input comparison method
                        if model_name == 'ground_truth' and "input" in case:
                            inp        = case["input"]
                            gt_res     = run_func_object(canonical_solution_code.get(task_id), inp)
                            if 'code_refinement_with_instructions' in mode or 'make_code_block' in mode:
                                model_res  = run_func_object(generated_solution_code.get(task_id), inp)
                            else:
                                model_res  = run_func_object(canonical_solution_code_no_contracts.get(task_id), inp)
                            assert_cnt = 1 
                        
                        elif "input" in case:
                            inp        = case["input"]
                            gt_res     = run_func_object(canonical_solution_code.get(task_id), inp)
                            model_res  = run_test_file(model_py, inp, model_name, test_cases_json)
                            assert_cnt = 1  
                
                        # (B) test_code(assert) method
                        else:
                            tcode      = case["test_code"]
                            gt_res     = run_func_with_tests(canonical_solution_code.get(task_id), tcode)
                            model_res  = run_file_with_tests(model_py, tcode)
                            assert_cnt = sum(1 for line in tcode.splitlines() if line.lstrip().startswith("assert"))
                        
                        # Success determination (maintain original logic)
                        if 'code_refinement_with_instructions' in mode or 'make_code_block' in mode:
                            error_message = ["Timeout", "InvalidInput", "AssertionError", "TypeError", "ValueError"]
                            if isinstance(model_res, str) and model_res.startswith(tuple(error_message)) and isinstance(gt_res, str) and gt_res.startswith("AssertionError"):
                                succ = False
                                assert_same = True
                            else:
                                print(f"gt_res: {gt_res}, model_res: {model_res}")
                                assert_same = False
                                succ = (model_res == gt_res)
                        else:
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
                            "assert_same":    assert_same,
                        })
                        
                per_task_runs[task_id].append(task_success)
                
            # contract, functionality determination score. If contract, functionality must be guaranteed. If functionality, contract + functionality must be guaranteed.
            combined_case_results = defaultdict(lambda: {'contract': [], 'functionality': []})
            # assertion error only pattern
            assertion_pattern = re.compile(r'^AssertionError:')
            # All *Error: pattern
            error_pattern = re.compile(r'^(?:[A-Za-z_]\w*Error|Exception):')
            
            for r in results:       
                key = (r['task_id'], r['section'], r['case_index'])
                gt_res    = str(r['groundtruth_result'])
                model_res = str(r['model_result'])
                
                # exclude input is empty
                if r.get('input') == None or r.get('input') == '' or (gt_res == None or model_res == None) or (gt_res == 'None' or model_res == 'None') or (gt_res == 'Timeout' and model_res == 'Timeout') or (gt_res == 'InvalidInput' and model_res == 'InvalidInput'):
                    continue
                
                # 1) GT is AssertionError case
                is_gt_assert = bool(assertion_pattern.match(gt_res))
                # 2) All *Error: message pattern
                is_model_error = bool(error_pattern.match(model_res))
                # 3) All *Error: message pattern
                is_gt_error    = bool(error_pattern.match(gt_res))
                
                if is_gt_assert and not is_model_error:
                    combined_case_results[key]['contract'].append(model_res == gt_res)
                elif (not is_gt_error) and (not is_model_error) : 
                    combined_case_results[key]['functionality'].append(model_res == gt_res)

            #per_task_runs[task_id].append(task_success)
            # contract-based pass@k calculation
            per_task_runs_contract = collapse_case_runs({k: v['contract'] for k, v in combined_case_results.items()})
            # functionality-based pass@k calculation
            per_task_runs_func     = collapse_case_runs({k: v['functionality'] for k, v in combined_case_results.items()})
            ######################################################################################################################
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
            
            
                
            # (4) pass@k CSV save
            total_tasks = len(per_task_runs)

            def compute_pass_at_k_dict(runs_dict, tag):
                result = {}
                for k in [1, 10, 100] if temp != 0.0 else [1]:
                    solved = sum(any(runs[:k]) for runs in runs_dict.values())
                    key = f"{tag}pass@{k}" if not (k == 1 and temp == 0.0) else f"{tag}pass@1*"
                    result[key] = (solved, len(runs_dict), solved / len(runs_dict) if runs_dict else 0.0)
                return result
            
            # partially filtered results
            metrics_contract = compute_pass_at_k_dict(per_task_runs_contract, tag='Contracts-')
            metrics_func = compute_pass_at_k_dict(per_task_runs_func, tag='Functionality-')
            metrics = {**metrics_contract, **metrics_func}
            order = list(metrics_contract.keys()) + list(metrics_func.keys())
            os.makedirs(output_path, exist_ok=True)

            # csv_path = os.path.join(model_out, f"{dataset_tag}_filtered_pass_at_k.csv")
            # with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
            #     writer = csv.writer(cf)
            #     writer.writerow(['metric', 'solved', 'total_tasks', 'rate'])
            #     for key in order:
            #         s, tot, r = metrics[key]
            #         writer.writerow([key, s, tot, f"{r:.2%}"])
                    
            ######################################################################################################################        
            # overall results
            metrics_all_2 = compute_pass_at_k_dict(per_task_runs, tag='All-')   
            metrics_contract_2 = compute_pass_at_k_dict(per_task_runs_contract_2, tag='Contracts-')
            metrics_func_2 = compute_pass_at_k_dict(per_task_runs_func_2, tag='Functionality-')
            metrics_2  = {**metrics_all_2, **metrics_contract_2, **metrics_func_2}
            order = list(metrics_all_2.keys()) + list(metrics_contract_2.keys()) + list(metrics_func_2.keys())
            os.makedirs(output_path, exist_ok=True)
            csv_path = os.path.join(model_out, f"{dataset_tag}_pass_at_k.csv")
            with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
                writer = csv.writer(cf)
                writer.writerow(['metric', 'solved', 'total_tasks', 'rate'])
                for key in order:
                    s, tot, r = metrics_2[key]
                    writer.writerow([key, s, tot, f"{r:.2%}"])
                    

            # 1. All saved results are already valid results
            total_test_cases = len(results)
            # 2. Number of failed cases
            total_failed_test_cases = len([r for r in results if not r['success']])
            # 3. assert-related statistics
            total_assert_cases = [r for r in results if is_assert_case(r)]
            non_assert_cases = [r for r in results if not is_assert_case(r)]
            
            #total_assert_cases = [r for r in results if isinstance(r['groundtruth_result'], str) and r['groundtruth_result'].startswith("Exception")]
            assert_len = len(total_assert_cases)
            assert_fail_len = len([r for r in total_assert_cases if not r['success']])
            assert_same_num = len([r for r in total_assert_cases if r['assert_same']])
            analysis_csv = os.path.join(model_out, f"{dataset_tag}_results_analysis_output.csv")
            
            non_assert_total = len(non_assert_cases)
            non_assert_success = len([r for r in non_assert_cases if not r['success']])
            
            #subset = [r for r in results if r['model'] == model_name]
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
                writer.writerow(['Assert-based testcases only', ''])
                writer.writerow(['Total assert-based testcases (GT)', assert_len])
                writer.writerow(['Failed assert-based testcases (GT)', assert_fail_len])
                writer.writerow(['Assert fail ratio (of assert-based)', f"{(assert_fail_len / assert_len * 100):.3f}%" if assert_len else "0.00%"])
                writer.writerow(['Same Assert of ground truth and generated code ratio (of assert-based)', f"{(assert_same_num / total_test_cases * 100):.3f}%" if total_test_cases else "0.00%"])
                writer.writerow(['', ''])
                writer.writerow(['Non-assert-based testcases only', ''])
                writer.writerow(['Total non-assert testcases', non_assert_total])
                writer.writerow(['Failed non-assert testcases', non_assert_success])
                writer.writerow(['Failed ratio (non-assert only)', f"{(non_assert_success / non_assert_total * 100):.3f}%" if non_assert_total else "0.00%"])
                writer.writerow(['', ''])
                writer.writerow(['Total tasks', num_tasks])
                
            star = test_case_model_name[0].split('_temp_')[-1] == '0.0'
            summarize_results(results, ks=[1, 10, 100], star_for_1=star)

            with open(os.path.join(model_out, f"{dataset_tag}_results.json"), 'w') as f:
                cleaned = make_json_serializable(subset)
                json.dump(cleaned, f, indent=2)
                
            if subset:
                with open(os.path.join(model_out, f"{dataset_tag}_results.csv"), 'w', newline='', encoding='utf-8') as cf:
                    try:
                        writer = csv.DictWriter(cf, fieldnames=subset[0].keys())
                        writer.writeheader()
                        writer.writerows(subset)
                    except:
                        writer = csv.DictWriter(cf,fieldnames=subset[0].keys(), quoting=csv.QUOTE_MINIMAL, doublequote=True,   escapechar="\\")
                        writer.writeheader()
                        writer.writerows(subset)
                    
            
            
            
            # save task_id only included in combined_case_results
            valid_runs     = set(combined_case_results.keys())
            combined_subset = [r for r in subset if (r['task_id'], r['section'], r['case_index']) in valid_runs]
            
            # # contract/functionality task_id based analysis_output save
            # combined_analysis_csv = os.path.join(model_out, f"{dataset_tag}_filtered_analysis_output.csv")
            # total_test_cases         = len(combined_subset)
            # total_failed_test_cases  = len([r for r in combined_subset if not r['success']])
            # total_assert_cases       = [r for r in combined_subset if is_assert_case(r)]
            # non_assert_cases         = [r for r in combined_subset if not is_assert_case(r)]
            # assert_len = len(total_assert_cases)
            # assert_fail_len = len([r for r in total_assert_cases if not r['success']])
            # non_assert_total = len(non_assert_cases)
            # non_assert_success = len([r for r in non_assert_cases if not r['success']])
            
            # unique_task_ids_combined = {r['task_id'] for r in combined_subset}
            # num_tasks_combined       = len(unique_task_ids_combined)
            # unique_task_ids_contract = set(per_task_runs_contract.keys())
            # num_tasks_contract_combined       = len(unique_task_ids_contract)
            # unique_task_ids_func     = set(per_task_runs_func.keys())
            # num_tasks_func_combined           = len(unique_task_ids_func)
            # with open(combined_analysis_csv, 'w', newline='', encoding='utf-8') as cf:
            #     writer = csv.writer(cf)
            #     writer.writerow(['Metric', 'Count'])
            #     writer.writerow(['Total test cases', total_test_cases])
            #     writer.writerow(['Total failed test cases', total_failed_test_cases])
            #     writer.writerow(['Total passed ratio (overall)', f"{((total_test_cases - total_failed_test_cases) / total_test_cases * 100):.3f}%" if total_test_cases else "0.00%"])
            #     writer.writerow(['Assert ratio (of all failed testcases)', f"{(assert_len / total_test_cases * 100):.3f}%" if total_test_cases else "0.00%"])
            #     writer.writerow(['', ''])
            #     writer.writerow(['Assert-based testcases only', ''])
            #     writer.writerow(['Total assert-based testcases (GT)', assert_len])
            #     writer.writerow(['Failed assert-based testcases (GT)', assert_fail_len])
            #     writer.writerow(['Assert fail ratio (of assert-based)', f"{(assert_fail_len / assert_len * 100):.3f}%" if assert_len else "0.00%"])
            #     writer.writerow(['', ''])
            #     writer.writerow(['Non-assert-based testcases only', ''])
            #     writer.writerow(['Total non-assert testcases', non_assert_total])
            #     writer.writerow(['Failed non-assert testcases', non_assert_success])
            #     writer.writerow(['Failed ratio (non-assert only)', f"{(non_assert_success / non_assert_total * 100):.3f}%" if non_assert_total else "0.00%"])
            #     writer.writerow(['', ''])
            #     writer.writerow(['Total tasks', num_tasks_combined])
            #     writer.writerow(['Total contract tasks', num_tasks_contract_combined])
            #     writer.writerow(['Total functionality tasks', num_tasks_func_combined])
                
            # with open(os.path.join(model_out, f"{dataset_tag}_filtered_results.json"), 'w') as f:
            #     cleaned = make_json_serializable(combined_subset)
            #     json.dump(cleaned, f, indent=2)
            
            
            indices = [
                {"task_id": r["task_id"], "section": r["section"], "case_index": r["case_index"]}
                for r in combined_subset
            ]

            data = test_cases
            model_key = test_cases_model_name

            # create filtered structure
            filtered = {}
            for idx in indices:
                task = idx['task_id']           # e.g. "HumanEval/3"
                section = idx['section']        # e.g. "assert_1"
                # case_index is 1-based, so convert to 0-based
                ci = idx['case_index'] - 1

                # nested dict initialize
                filtered.setdefault(task, {})
                filtered[task].setdefault(section, [])

                # extract corresponding entry
                entries = data.get(task, {}).get(section, [])
                if 0 <= ci < len(entries):
                    filtered[task][section].append(entries[ci])

            # wrap final structure and save file
            # out = {model_key: filtered}
            # with open(os.path.join(model_out,f"{dataset_tag}_filtered_results_filtered.json"), 'w', encoding='utf-8') as f:
            #     json.dump(out, f, ensure_ascii=False, indent=2)
                    
            
            
            # if combined_subset:
            #     with open(os.path.join(model_out, f"{dataset_tag}_filtered_results.csv"), 'w', newline='', encoding='utf-8') as cf:
            #         writer = csv.DictWriter(cf, fieldnames=combined_subset[0].keys())
            #         writer.writeheader()
            #         writer.writerows(combined_subset)

            # define function to save filtered structure (internal function)
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
                    if 0 <= ci < len(entries):
                        filtered[task][section].append(entries[ci])
                out = {test_cases_model_name: filtered}
                with open(out_path, 'w', encoding='utf-8') as f:
                    json.dump(out, f, ensure_ascii=False, indent=2)

            # # save contract-based subset (filtered structure)
            # if mode == 'before_quality_check':
            #     combined_subset_contract = [
            #         r for r in subset
            #         if (r['task_id'], r['section'], r['case_index']) in combined_case_results
            #         and combined_case_results[(r['task_id'], r['section'], r['case_index'])]['contract']
            #     ]
            #     save_filtered_json(combined_subset_contract, os.path.join(model_out, f"{dataset_tag}_contracts_results_filtered.json"))

            #     combined_subset_func = [
            #         r for r in subset
            #         if (r['task_id'], r['section'], r['case_index']) in combined_case_results
            #         and combined_case_results[(r['task_id'], r['section'], r['case_index'])]['functionality']
            #     ]
            #     save_filtered_json(combined_subset_func, os.path.join(model_out, f"{dataset_tag}_functionality_results_filtered.json"))

    
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
                        tid = row['task_id']            # current task ID
                        cnt = row.get('assert_cnt', 1)  # if assert-based, number of lines, otherwise 1

                        if row['success']:
                            task_stats[tid]['succ'] = cnt   # replace += with =
                            task_stats[tid]['fail'] = 0     # opposite item is 0
                        else:
                            task_stats[tid]['succ'] = 0
                            task_stats[tid]['fail'] = cnt
                
                sum_csv = os.path.join(model_out, f"{dataset_tag}_per_task_summary.csv")
                with open(sum_csv, 'w', newline='', encoding='utf-8') as cf:
                    w = csv.writer(cf)

                    # 1) define header
                    header = ['task_id', 'success_cnt', 'fail_cnt', 'total', 'success_rate']
                    if temp == 0.0:
                        header.append('pass@1*')
                    else:
                        header.extend(['pass@1', 'pass@10', 'pass@100'])
                    w.writerow(header)

                    # 2) write each task row
                    for task_id in sorted(task_stats, key=lambda x: int(x.split('/')[1])):
                        s = task_stats[task_id]['succ']
                        f = task_stats[task_id]['fail']
                        tot = s + f
                        rate = f"{(s / tot):.2%}" if tot else "0.00%"

                        # pass@k calculation (per_task_runs is already filled above)
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

def json_format_output():
    json_result = {"Data_total_len": 0, 
                "Data_total_generation": 0, 
                "Score": {
                    "functionality": 0.0,
                    "contracts": 0.0,
                    "AAR": 0.0,
                    "AAP": 0.0,
                    "total": 0.0,    
                    "gt_contract_check": 0.0,
                },
                'Score_percent':{
                    "functionality": 0.0,
                    "contracts": 0.0,
                    "AAR": 0.0,
                    "AAP": 0.0,
                    "total": 0.0,    
                    "gt_contract_check": 0.0,
                },
                "functionality": {},
                "contracts": {},
                "AAR": {},
                "AAP": {},
                "total": {},
                "gt_contract_check": {},
    }
    return json_result
    

def load_existing_results(out_path):
    results = {
        'json_result': None,
        'humaneval_result': None, 
        'mbpp_result': None,
        'generated_func_dict': {},
        'compile_stats': {
            "attempted": 0,
            "humaneval_compile": 0,
            "mbpp_compile": 0,
            "success": 0,
            "humaneval_compile_success": 0,
            "mbpp_compile_success": 0,
            "success_rate_percent": 0.0,
            "failed": [],
        }
    }
    
    try:
        if os.path.exists(f"{out_path}/total_results.json"):
            with open(f"{out_path}/total_results.json", 'r') as f:
                results['json_result'] = json.load(f)
        
        if os.path.exists(f"{out_path}/humaneval_results.json"):
            with open(f"{out_path}/humaneval_results.json", 'r') as f:
                results['humaneval_result'] = json.load(f)
                
        if os.path.exists(f"{out_path}/mbpp_results.json"):
            with open(f"{out_path}/mbpp_results.json", 'r') as f:
                results['mbpp_result'] = json.load(f)
                
        if os.path.exists(f"{out_path}/generated_func_dict.json"):
            with open(f"{out_path}/generated_func_dict.json", 'r') as f:
                results['generated_func_dict'] = json.load(f)
                
        if os.path.exists(f"{out_path}/compile_stats.json"):
            with open(f"{out_path}/compile_stats.json", 'r') as f:
                results['compile_stats'] = json.load(f)
                
    except Exception as e:
        print(f"⚠️ Error loading existing results: {e}")
        
    return results

def save_progress(out_path, json_result, humaneval_result, mbpp_result, generated_func_dict, compile_stats):

    try:
        with open(f"{out_path}/total_results.json", 'w') as f:
            json.dump(json_result, f, indent=2)
            
        with open(f"{out_path}/humaneval_results.json", 'w') as f:
            json.dump(humaneval_result, f, indent=2)
            
        with open(f"{out_path}/mbpp_results.json", 'w') as f:
            json.dump(mbpp_result, f, indent=2)
            
        with open(f"{out_path}/generated_func_dict.json", 'w') as f:
            json.dump(generated_func_dict, f, indent=2)
            
        with open(f"{out_path}/compile_stats.json", 'w') as f:
            json.dump(compile_stats, f, indent=2)
            
    except Exception as e:
        print(f"⚠️ error occurred while saving progress: {e}")

if __name__ == '__main__':
    random.seed(42) 
    parser = argparse.ArgumentParser()
    parser.add_argument('--code_generation_model_path', type=str, required=True, help='Path to code generation model')
    parser.add_argument('--code_generation_model_name', type=str, required=True, help='Name of code generation model')
    parser.add_argument('--humaneval_functionality_dataset_path', type=str, required=True, help='Path to functionality dataset')
    parser.add_argument('--mbpp_functionality_dataset_path', type=str, required=True, help='Path to functionality dataset')
    parser.add_argument('--humaneval_contracts_dataset_path', type=str, required=True, help='Path to contracts dataset')
    parser.add_argument('--mbpp_contracts_dataset_path', type=str, required=True, help='Path to contracts dataset')
    parser.add_argument('--output_path', type=str, required=True, help='Output directory')
    parser.add_argument('--mode', type=str, required=True, help='Mode')
    parser.add_argument('--use_None_list', type=str, required=True, help='Use None list')
    parser.add_argument('--contract_test_case_type', type=str, required=True, help='Contract test case type')
    args = parser.parse_args()

    
    if "!next!" in args.code_generation_model_path:
        code_generation_model_path = [i.strip() for i in args.code_generation_model_path.split("!next!")]
    else:
        code_generation_model_path = [args.code_generation_model_path]
    
    
    print("="*100)
    print(f"Code generation model name: {args.code_generation_model_name}")
    print(f"Code generation path: {code_generation_model_path}")
    print("output path: {args.output_path}")
    print("="*100)
    
    # load class
    rewarder = EvaluationRewarder(
        humaneval_functionality_dataset_path=args.humaneval_functionality_dataset_path,
        mbpp_functionality_dataset_path=args.mbpp_functionality_dataset_path,
        humaneval_contracts_dataset_path=args.humaneval_contracts_dataset_path,
        mbpp_contracts_dataset_path=args.mbpp_contracts_dataset_path,
        contract_test_case_type=args.contract_test_case_type,
    )
    
    
    # gold test dataset
    # if args.mode == "full_check":
    gold_test_dataset_dict={}
    with open("../../data/code_generation/total/CODE_GENERATION_CT/o4-mini/total.jsonl", 'r') as f:
        for line in f:
            data = json.loads(line)
            gold_test_dataset_dict[data['name']] = ['check']
    # else:
    #     gold_test_dataset_dict={}
    #     with open("../../data/code_generation/total/CODE_GENERATION_CS/o4-mini/test.jsonl", 'r') as f:
    #         for line in f:
    #             data = json.loads(line)
    #             gold_test_dataset_dict[data['name']] = ['check']
    
    
    code_generation_dict={}
    
    # our, full
    if len(code_generation_model_path) == 1:
        for code_generation_model_path in code_generation_model_path:
            if code_generation_model_path.endswith('.jsonl'):
                try:
                    with open(code_generation_model_path, 'r') as f:
                        for line in f:
                            data = json.loads(line)
                            code_generation_dict[data['name']] = {"outputs": [data['grammar'][0]]}
                except:
                    # this is our branch generation type (full)
                    code_generation_model_path = code_generation_model_path.replace('.jsonl', '.json')
                    with open(code_generation_model_path, 'r') as f:
                        data = json.load(f)
                        for set, value in data.items():
                            if set == "Setting":
                                continue
                            for i in value:
                                code_generation_dict[i['task_id']] = {"outputs": [i['outputs'][0]]}
    
    #base
    else:
        for path in code_generation_model_path:
            with open(path, 'r') as f:
                load_data= json.load(f)
                data = load_data[args.code_generation_model_name]
                for i in data:
                    if isinstance(i['task_id'], list):
                        task_id = i['task_id'][0]
                    else:
                        task_id = i['task_id']

                    if task_id in gold_test_dataset_dict.keys():
                        code_generation_dict[task_id] = i
    
    if code_generation_dict.keys() != gold_test_dataset_dict.keys():
        print(f"Error: code_generation_dict and gold_test_dataset_dict have different keys")
        not_in_key =[]
        for key in gold_test_dataset_dict.keys():
            if key not in code_generation_dict.keys():
                not_in_key.append(key)
        print(f"not in key: {not_in_key}")
        pdb.set_trace()
    

    json_result = json_format_output()
    humaneval_result = json_format_output()
    mbpp_result = json_format_output()
    
    json_result["Data_total_len"] = len(gold_test_dataset_dict)
    json_result["Data_total_generation"] = len(code_generation_dict)
    
    humaneval_result["Data_total_len"] = len([i for i in gold_test_dataset_dict.keys() if 'HumanEval' in i])
    humaneval_result["Data_total_generation"] = len([i for i in code_generation_dict.keys() if 'HumanEval' in i])
    
    mbpp_result["Data_total_len"] = len([i for i in gold_test_dataset_dict.keys() if 'Mbpp' in i])
    mbpp_result["Data_total_generation"] = len([i for i in code_generation_dict.keys() if 'Mbpp' in i])
    

    out_path = args.output_path
    if os.path.isdir(out_path) or out_path.endswith(os.sep):
        os.makedirs(out_path, exist_ok=True)
    
    existing_results = load_existing_results(out_path)
    

    if existing_results['json_result']:
        print("🔄 load existing results.")
        json_result = existing_results['json_result']
        humaneval_result = existing_results['humaneval_result'] or humaneval_result
        mbpp_result = existing_results['mbpp_result'] or mbpp_result
        generated_func_dict = existing_results['generated_func_dict']
        compile_stats = existing_results['compile_stats']
    else:
        compile_stats = {
            "attempted": 0,
            "humaneval_compile": 0,
            "mbpp_compile": 0,
            "success": 0,
            "humaneval_compile_success": 0,
            "mbpp_compile_success": 0,
            "success_rate_percent": 0.0,
            "failed": [],
        }
        generated_func_dict = {}
    
    from builtins import set as bset
    processed_task_ids = bset(json_result.get("functionality", {}).keys())
    all_task_ids = bset(list(code_generation_dict.keys()))
    remaining_task_ids = all_task_ids - processed_task_ids
    
    print(f"📊 total tasks: {len(all_task_ids)}")
    print(f"✅ already processed: {len(processed_task_ids)}")
    print(f"⏳ remaining tasks: {len(remaining_task_ids)}")
    
    if not remaining_task_ids:
        print("🎉 all tasks are already processed!")
        exit()
    
    for task_id, value in tqdm([(tid, code_generation_dict[tid]) for tid in sorted(remaining_task_ids)], 
                               total=len(remaining_task_ids), desc="Processing"):
        
        try:
            functionality_reward, contracts_reward, aar, aap, total_reward, details, generated_func = rewarder.reward(args.code_generation_model_path,task_id, value['outputs'][0])
        except Exception as e:
            functionality_reward, contracts_reward, aar, aap, total_reward, details, generated_func = 0.0, 0.0, 0.0, 0.0, 0.0, {"error": str(e)}, None
        generated_func_dict[task_id] = {"inference": value['outputs'][0], "parsed_func": generated_func}
        
        # Direct compile() check on the parsed generated code (no GT dependency)
        if isinstance(generated_func, str) and generated_func.strip():
            compile_stats["attempted"] += 1
            if 'HumanEval' in task_id:
                compile_stats["humaneval_compile"] += 1
            elif 'Mbpp' in task_id:
                compile_stats["mbpp_compile"] += 1
            try:
                compile(generated_func, "<generated_code>", "exec")
                compile_stats["success"] += 1
                if 'HumanEval' in task_id:
                    compile_stats["humaneval_compile_success"] += 1
                elif 'Mbpp' in task_id:
                    compile_stats["mbpp_compile_success"] += 1
            except Exception as e:
                compile_stats["failed"].append({"task_id": task_id, "error": str(e)})
        
        print('--------------------------------')
        print(f"Task ID: {task_id}, Functionality Reward: {functionality_reward}, Contracts Reward: {contracts_reward}, AAR: {aar}, AAP: {aap}, Total Reward: {total_reward}")
        print("\ndetails:", details)
        print('--------------------------------\n\n')
        
        json_result["functionality"][task_id] = functionality_reward
        json_result["contracts"][task_id] = contracts_reward
        json_result["AAR"][task_id] = aar
        json_result["AAP"][task_id] = aap
        json_result["gt_contract_check"][task_id] = float(details.get('gt_contracts_check', 0.0)) if isinstance(details, dict) else 0.0
        json_result["total"][task_id] = total_reward
        
        if "HumanEval" in task_id:
            humaneval_result["functionality"][task_id] = functionality_reward
            humaneval_result["contracts"][task_id] = contracts_reward
            humaneval_result["AAR"][task_id] = aar
            humaneval_result["AAP"][task_id] = aap
            humaneval_result["gt_contract_check"][task_id] = float(details.get('gt_contracts_check', 0.0)) if isinstance(details, dict) else 0.0
            humaneval_result["total"][task_id] = total_reward
            
        elif "Mbpp" in task_id:
            mbpp_result["functionality"][task_id] = functionality_reward
            mbpp_result["contracts"][task_id] = contracts_reward
            mbpp_result["AAR"][task_id] = aar
            mbpp_result["AAP"][task_id] = aap
            mbpp_result["gt_contract_check"][task_id] = float(details.get('gt_contracts_check', 0.0)) if isinstance(details, dict) else 0.0
            mbpp_result["total"][task_id] = total_reward
        
        save_progress(out_path, json_result, humaneval_result, mbpp_result, generated_func_dict, compile_stats)
        print(f"💾 {task_id} processed and saved")

    # calculate success rate
    compile_stats["success_rate_percent"] = (compile_stats["success"] / compile_stats["attempted"] * 100) if compile_stats["attempted"] else 0.0

    # Average scores over generated items; fallback to dataset length if zero
    denom = json_result["Data_total_len"]
    humaneval_denom = humaneval_result["Data_total_len"]
    mbpp_denom = mbpp_result["Data_total_len"]
    for key in ["functionality", "contracts", "AAR", "AAP", "total", "gt_contract_check"]:
        vals = [v for v in json_result[key].values() if isinstance(v, (int, float))]
        human_vals=[v for v in humaneval_result[key].values() if isinstance(v, (int, float))]
        mbpp_vals=[v for v in mbpp_result[key].values() if isinstance(v, (int, float))]
        
        json_result["Score"][key] = (sum(vals)) if vals else 0.0
        json_result["Score_percent"][key] = (sum(vals) / denom) if vals else 0.0
        
        humaneval_result["Score"][key] = (sum(human_vals)) if human_vals else 0.0
        humaneval_result["Score_percent"][key] = (sum(human_vals) / humaneval_denom) if human_vals else 0.0
        
        mbpp_result["Score"][key] = (sum(mbpp_vals)) if mbpp_vals else 0.0
        mbpp_result["Score_percent"][key] = (sum(mbpp_vals) / mbpp_denom) if mbpp_vals else 0.0  

    print("="*100)
    print(f"Data_total_len: {json_result['Data_total_len']}")
    print(f"Data_total_generation: {json_result['Data_total_generation']}")
    print(f"Score: {json_result['Score_percent']}")
    print("="*100)

    # save final results
    save_progress(out_path, json_result, humaneval_result, mbpp_result, generated_func_dict, compile_stats)
    print(f"💾 {out_path}/total_results.json")
    print(f"🎉 all tasks are processed and saved to {out_path}")
        