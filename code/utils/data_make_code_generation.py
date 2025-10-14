import json
import argparse
from typing import Any, Dict, Optional
from pathlib import Path
from Instruction import instruction_template
import pdb
import re
import textwrap
import inspect
from sklearn.model_selection import train_test_split
import os

def load_dataset(dataset_name, testcase_path): # testcase_path -> CT
    if dataset_name == "humaneval":
        # This is use for instruction -> CS
        code_generation_data_path = '../../code/output_gpt/original/gpt-4o-mini/code_generation/humaneval_gpt-4o-mini_sft.jsonl'
        # This is use for canonical solution
        original_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'

    elif dataset_name == "mbpp":
        # This is use for instruction -> CS
        code_generation_data_path = '../../code/output_gpt/original/gpt-4o-mini/code_generation/mbpp_gpt-4o-mini_sft.jsonl'
        # This is use for canonical solution
        original_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'        
    
    code_generation_data = {}
    with open(code_generation_data_path, 'r') as f:
        for line in f:
            try:
                code_generation_data[json.loads(line)['name']] = json.loads(line)
            except:
                if "\\zn" in line:
                    line = line.replace("\\zn", "\\n")
                code_generation_data[json.loads(line)['name']] = json.loads(line)
    
    with open(testcase_path, 'r') as f:
        full_testcase_data = json.load(f)
        testcase_data = full_testcase_data['contract_check_results']
    
    original_data = {}
    with open(original_path, 'r') as f:
        for line in f:
            original_data[json.loads(line)['task_id']] = json.loads(line)
    
    
    print("✅ Successfully loaded code generation data: {}, \n{}".format(len(code_generation_data), code_generation_data_path))
    print("✅ Successfully loaded testcase data: {}, \n{}".format(len(testcase_data), testcase_path))
    print("✅ Successfully loaded original data: {}, \n{}".format(len(original_data), original_path))
    print("="*100)
    
    return code_generation_data, testcase_data, original_data

def safe_eval(input_dict):
    """Safe evaluation of input strings."""
    
    for key, value in input_dict.items():
        if isinstance(value, str):
            input_dict[key] = (value
                 .replace("null", "None")
                 .replace("true", "True")
                 .replace("false", "False"))

    return input_dict

# Normalize contract_in_key which can be a single string like 'assert_2',
# a delimited string like 'assert_1;assert_2', or a list of such values.
# Returns a list of non-empty string keys without duplicates in order.
def _normalize_contract_keys(contract_key_value):
    if contract_key_value is None:
        return []
    if isinstance(contract_key_value, list):
        result = []
        for k in contract_key_value:
            s = str(k).strip()
            if not s:
                continue
            if s not in result:
                result.append(s)
        return result
    if isinstance(contract_key_value, str):
        parts = re.split(r'[;,\s]+', contract_key_value.strip())
        result = []
        for p in parts:
            if not p:
                continue
            if p not in result:
                result.append(p)
        return result
    # Fallback to single coerced string
    s = str(contract_key_value).strip()
    return [s] if s else []

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
    

def _clean_docstring_blocks(code: str) -> str:
    code = re.sub(r"```.*?```", "", code, flags=re.DOTALL)
    code = re.sub(r'(def[^\n]+\n)\s*""".*?"""\n', r'\1', code, flags=re.DOTALL)
    return code.strip()

def _is_executable(code: str) -> bool:
    try:
        compiled = compile(code, "<string>", "exec")
        exec(compiled, {})
        return True
    except Exception as e:
        print(f"[WARN] Code execution failed: {e}")
        return False

def _get_param_order_from_code(code: str, entry_point: str) -> list[str]:
    """Return parameter names in the order defined by the function signature.
    Try exec + inspect first, then fall back to a regex parse of the def header."""
    try:
        ns: dict[str, Any] = {}
        exec(compile(code, "<string>", "exec"), ns)
        fn = ns.get(entry_point)
        if callable(fn):
            return list(inspect.signature(fn).parameters.keys())
    except Exception:
        pass

    pat = rf'^\s*def\s+{re.escape(entry_point)}\s*\((.*?)\)\s*:'
    m = re.search(pat, code, flags=re.MULTILINE | re.DOTALL)
    if not m:
        return []
    params_blob = m.group(1)
    parts = [p.strip() for p in params_blob.split(',') if p.strip()]
    ordered: list[str] = []
    for p in parts:
        name = p.split('=')[0].strip().lstrip('*')
        if name:
            ordered.append(name)
    return ordered

def canonical_solution_load(original_data, task_id, dataset):   
    prompt = original_data[task_id]['prompt']
    contract = original_data[task_id]['contract']
    canonical_solution = original_data[task_id]['canonical_solution']
    entry_point = original_data[task_id]['entry_point']
   
    if dataset == 'humaneval':
        full_code = f"{prompt}\n{contract}\n{canonical_solution}"
        full_code = _clean_docstring_blocks(full_code)
    elif dataset == 'mbpp':
        full_code = _inject_contracts_into_solution(canonical_solution, contract, entry_point)

    if not _is_executable(full_code):
        print(f"[ERROR] canonical_solution for {dataset}/{task_id} is not executable")
        pdb.set_trace()
    
    return full_code

def code_generation_template_dataset(code_generation_data, testcase_data, original_data, mode='CODE_GENERATION_CS', dataset='humaneval'):
    system, user_tail = instruction_template(mode)
    create_dataset = []
    input_contract_test_cases = {}
    
    
    #if mode == "CODE_GENERATION_CT":
    reasoning_path="../../code/output_gpt/original/o4-mini/code_generation_ct"
    if os.path.exists(f"{reasoning_path}/{dataset}_o4-mini_sft.jsonl"):
        reasoning_data = {}
        with open(f"{reasoning_path}/{dataset}_o4-mini_sft.jsonl", 'r') as f:
            for line in f:
                reasoning_data[json.loads(line)['name']] = json.loads(line)['reasoning']
        print("✅ Successfully loaded reasoning")
    #else:
    #    reasoning_data = None
    
    for task_id, value in code_generation_data.items():
        
        # data normalization
        if task_id not in reasoning_data.keys():
            continue
        
        
        name = task_id
        grammar_production = code_generation_data[task_id]['grammar'][0]['production'][0]
        grammar_constraints = code_generation_data[task_id]['grammar'][0]['constraints'][0]
        canonical_solution = canonical_solution_load(original_data, task_id, dataset)
        
        # System
        description_system_content = system
        
        # User
        entry_point = original_data[task_id]['entry_point']
        
        # Prepare for contract test cases
        input_contract_test_cases[task_id] = {}
        for contract_key in grammar_constraints.keys():
            input_contract_test_cases[task_id][contract_key] = {'section':[], 'case_index':[], 'test_case':[], 'test_case_instruction':[]}
        
        
        try:
            param_cnt = len(inspect.signature(canonical_solution).parameters) if callable(canonical_solution) else None
        except Exception:
            param_cnt = None
        
        # Determine parameter order from the canonical solution
        param_order = _get_param_order_from_code(canonical_solution, entry_point)
        used_case_indices = set()
        
        # contract test case (only for CT)
        if mode == "CODE_GENERATION_CT":
            for contract_section in testcase_data.get(task_id, {}):
                # Not SMT test castaske
                if testcase_data[task_id][contract_section] != {}:
                    for task_id_2, contract_test_case_list in testcase_data[task_id][contract_section].items():
                        for contract_test_case in contract_test_case_list:
                            
                            contract_in_key = contract_test_case['contract_in_key']
                            model_result = contract_test_case['model_result']
                            test_case = contract_test_case['input']
                            case_index = contract_test_case['case_index']
                            
                        
                            if isinstance(model_result, str):
                                if model_result.startswith("AssertionError") and input_contract_test_cases[task_id][contract_in_key]['section'] == []:
                                    # Skip if already selected by another contract key
                                    if f"{contract_section}:{case_index}" in used_case_indices:
                                        continue
                                    
                                    input_contract_test_cases[task_id][contract_in_key]['section'].append(contract_section)
                                    input_contract_test_cases[task_id][contract_in_key]['case_index'].append(case_index)
                                    input_contract_test_cases[task_id][contract_in_key]['test_case'].append(test_case)
        
                                    # Safely parse textual Python literals (e.g., "('a', 1)")
                                    test_case = safe_eval(test_case)
                                    
                                    # Order the dict keys according to the function signature; append unknown keys afterwards
                                    ordered_keys = [k for k in param_order if k in test_case]
                                    args_str = ', '.join(f"{repr(test_case[k])}" for k in ordered_keys)
                                    input_contract_test_cases[task_id][contract_in_key]['test_case_instruction'].append(f'{contract_in_key}:\n>>> {entry_point}({args_str})\n "AssertionError: invalid input"\n')
                                    used_case_indices.add(f"{contract_section}:{case_index}")
            
                                
            # Fallback: if a contract_key has no test case, add a None-based placeholder assertion
            has_any_case = any(len(_rec['test_case_instruction']) > 0 for _rec in input_contract_test_cases[task_id].values())
            if has_any_case:
                for _ck, _rec in input_contract_test_cases[task_id].items():
                    if _rec['test_case_instruction'] == []:
                        _rec['section'].append('no_test_case')
                        _rec['case_index'].append(-1)
                        _rec['test_case'].append(None)
                        _args_str = ', '.join(['None' for _ in (param_order or [])]) if param_order is not None else ''
                        _rec['test_case_instruction'].append(f'{_ck}: no suitable test case\n')
            
            
                                
            input_contract_test_case_str = ""
            for contract_key in input_contract_test_cases[task_id].keys():
                for test_case_instruction in input_contract_test_cases[task_id][contract_key]['test_case_instruction']:
                    input_contract_test_case_str += f"{test_case_instruction}\n"

            if input_contract_test_case_str == "":
                del input_contract_test_cases[task_id]
                continue
            
        if mode == "CODE_GENERATION_CS":
            description_user_content = (
                f"Method Name: {entry_point}\n"
                f"Problem Description:\n{grammar_production}\n"
                f"{user_tail}"
            )
        elif mode == "CODE_GENERATION_CT":
            description_user_content = (
                f"Method Name: {entry_point}\n"
                f"Problem Description:\n{grammar_production}\n"
                f"\nAll assert statements for {[i for i in input_contract_test_cases[task_id].keys()]}: \n"
                f"\nContract Test Cases:\n{input_contract_test_case_str}"
                f"{user_tail}"
            )
        # print(description_user_content)
        # pdb.set_trace()
        
        
        #if mode == "CODE_GENERATION_CT":
        reasoning = reasoning_data[task_id][0]
        # else:
        #    reasoning = "I have done a short CoT reasoning and Aha! I have found the right answer.\n</think>\n\n"
        
            
                
        
        template = {
            "name": name,
            "description": [
                {"role": "system", "content": description_system_content},
                {"role": "user", "content": description_user_content},
            ],
            "grammar": [{
                "production": canonical_solution,
                "constraints": grammar_constraints,
            }],
            "reasoning": [reasoning],
        }
        
        create_dataset.append(template)
        
    if mode == "CODE_GENERATION_CS":
        return create_dataset, None
    elif mode == "CODE_GENERATION_CT":
        return create_dataset, input_contract_test_cases


def save_jsonl(data, output_path, mode):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(f"{output_path}/{mode}.jsonl", 'w') as f:
        for item in data:
            try:
                f.write(json.dumps(item) + '\n')
            except Exception as e:
                print(f"❌ [{item['name']}] Error saving JSONL: {e}")
                pdb.set_trace()

def save_json(data, output_path, mode):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(f"{output_path}/{mode}.json", 'w') as f:
        json.dump(data, f, indent=4)

def train_valid_split(data, valid_ratio=0.1):
    train_rows, valid_rows = train_test_split(
        data,
        test_size=valid_ratio,
        random_state=42,
        shuffle=True,
    )

    return train_rows, valid_rows

def prune_testcase_data(testcase_data, input_contract_test_cases):
    pruned = {}
    for task_id, sections in testcase_data.items():
        
        # Build removal map for this task_id: section -> set(case_index)
        removal_map = {}
        task_cases = input_contract_test_cases.get(task_id, {}) if isinstance(input_contract_test_cases, dict) else {}
        for contract_key, data in task_cases.items():
            sections_list = data.get('section', [])
            indices_list = data.get('case_index', [])

            for sec, idx in zip(sections_list, indices_list):
                if sec not in removal_map:
                    removal_map[sec] = set()
                removal_map[sec].add(idx)
        # Apply filtering per section
        pruned_sections = {}
        for section, inner in sections.items():
            if inner == {}:
                # Skip empty section entirely
                continue
            remove_indices = removal_map.get(section, set())
            pruned_inner = {}
            for inner_key, case_list in inner.items():
                if not isinstance(case_list, list):
                    # Keep only non-empty non-list entries
                    if case_list != {}:
                        pruned_inner[inner_key] = case_list
                    continue
                # Keep only cases that:
                # 1) are NOT selected (case_index not in remove_indices)
                # 2) have model_result that is an AssertionError
                # Then deduplicate by case_index (keep first) and aggregate duplicate contract_in_key values
                filtered_list = []
                seen_indices: dict[int, dict] = {}
                for case in case_list:
                    idx = case.get('case_index')
                    model_result = case.get('model_result')
                    is_assert_error = isinstance(model_result, str) and model_result.startswith("AssertionError")
                    if idx in remove_indices:
                        continue
                    if not is_assert_error:
                        continue
                    if idx is not None:
                        if idx not in seen_indices:
                            keys_agg = _normalize_contract_keys(case.get('contract_in_key'))
                            case['contract_in_key'] = ';'.join(keys_agg)
                            seen_indices[idx] = {'case': case, 'keys': keys_agg}
                            filtered_list.append(case)
                        else:
                            dup_keys = _normalize_contract_keys(case.get('contract_in_key'))
                            keys_agg = seen_indices[idx]['keys']
                            for k in dup_keys:
                                if k not in keys_agg:
                                    keys_agg.append(k)
                            seen_indices[idx]['case']['contract_in_key'] = ';'.join(keys_agg)
                        continue
                    else:
                        keys_agg = _normalize_contract_keys(case.get('contract_in_key'))
                        case['contract_in_key'] = ';'.join(keys_agg)
                        filtered_list.append(case)
                if filtered_list:
                    pruned_inner[inner_key] = filtered_list
            if pruned_inner:
                pruned_sections[section] = pruned_inner
        # Only keep task_id if there is at least one non-empty section after pruning
        if pruned_sections:
            pruned[task_id] = pruned_sections
    return pruned


def assertion_only_dedup_testcase_data(testcase_data):
    total = {}
    for task_id, sections in testcase_data.items():
        total[task_id] = {}
        for section, inner in sections.items():
            if inner == {}:
                total[task_id][section] = inner
                continue
            pruned_inner = {}
            for inner_key, case_list in inner.items():
                if not isinstance(case_list, list):
                    pruned_inner[inner_key] = case_list
                    continue
                filtered_list = []
                seen_indices: dict[int, dict] = {}
                for case in case_list:
                    idx = case.get('case_index')
                    model_result = case.get('model_result')
                    is_assert_error = isinstance(model_result, str) and model_result.startswith("AssertionError")
                    if not is_assert_error:
                        continue
                    if idx is not None:
                        if idx not in seen_indices:
                            keys_agg = _normalize_contract_keys(case.get('contract_in_key'))
                            case['contract_in_key'] = ';'.join(keys_agg)
                            seen_indices[idx] = {'case': case, 'keys': keys_agg}
                            filtered_list.append(case)
                        else:
                            dup_keys = _normalize_contract_keys(case.get('contract_in_key'))
                            keys_agg = seen_indices[idx]['keys']
                            for k in dup_keys:
                                if k not in keys_agg:
                                    keys_agg.append(k)
                            seen_indices[idx]['case']['contract_in_key'] = ';'.join(keys_agg)
                        continue
                    else:
                        keys_agg = _normalize_contract_keys(case.get('contract_in_key'))
                        case['contract_in_key'] = ';'.join(keys_agg)
                        filtered_list.append(case)
                pruned_inner[inner_key] = filtered_list
            total[task_id][section] = pruned_inner
    return total

def _exec_get_entry_function(code: str, entry_point: str):
    ns: Dict[str, Any] = {}
    exec(compile(code, "<string>", "exec"), ns)
    fn = ns.get(entry_point)
    if not callable(fn):
        raise ValueError(f"Entry point '{entry_point}' not found or not callable")
    return fn


def _coerce_input_to_python(obj):
    # Accept dict (already structured), JSON-like string, or Python-literal string
    if isinstance(obj, dict):
        return safe_eval(obj)
    if isinstance(obj, str):
        txt = obj.replace("null", "None").replace("true", "True").replace("false", "False")
        try:
            import ast
            return ast.literal_eval(txt)
        except Exception:
            # Fall back to raw string
            return obj
    return obj


def _run_func_gt(fn, inp):
    try:
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        if isinstance(inp, dict):
            args = []
            for name in params:
                if name in inp:
                    args.append(inp[name])
                else:
                    # Missing parameter; let it raise to mark as non-assert
                    raise KeyError(name)
            fn(*args)
        elif isinstance(inp, (list, tuple)):
            fn(*inp)
        else:
            fn(inp)
        return None
    except AssertionError as e:
        return f"AssertionError: {e}"
    except Exception as e:
        return f"Exception: {e}"


def assertion_only_dedup_testcase_data_gt(testcase_data, original_data, dataset):
    total = {}
    for task_id, sections in testcase_data.items():
        total[task_id] = {}
        try:
            entry_point = original_data[task_id]['entry_point']
            full_code = canonical_solution_load(original_data, task_id, dataset)
            gt_fn = _exec_get_entry_function(full_code, entry_point)
        except Exception as e:
            # Skip this task if GT cannot be built
            continue

        for section, inner in sections.items():
            if inner == {}:
                total[task_id][section] = inner
                continue
            pruned_inner = {}
            for inner_key, case_list in inner.items():
                if not isinstance(case_list, list):
                    pruned_inner[inner_key] = inner_key if inner_key != {} else {}
                    continue
                filtered_list = []
                seen_indices: Dict[int, Dict] = {}
                for case in case_list:
                    raw_inp = case.get('input') or case.get('test_case')
                    coerced = _coerce_input_to_python(raw_inp)
                    res = _run_func_gt(gt_fn, coerced)
                    is_assert_error = isinstance(res, str) and res.startswith("AssertionError")
                    if not is_assert_error:
                        continue

                    idx = case.get('case_index')
                    if idx is not None:
                        if idx not in seen_indices:
                            keys_agg = _normalize_contract_keys(case.get('contract_in_key'))
                            case['contract_in_key'] = ';'.join(keys_agg)
                            seen_indices[idx] = {'case': case, 'keys': keys_agg}
                            filtered_list.append(case)
                        else:
                            dup_keys = _normalize_contract_keys(case.get('contract_in_key'))
                            keys_agg = seen_indices[idx]['keys']
                            for k in dup_keys:
                                if k not in keys_agg:
                                    keys_agg.append(k)
                            seen_indices[idx]['case']['contract_in_key'] = ';'.join(keys_agg)
                        continue
                    else:
                        keys_agg = _normalize_contract_keys(case.get('contract_in_key'))
                        case['contract_in_key'] = ';'.join(keys_agg)
                        filtered_list.append(case)
                pruned_inner[inner_key] = filtered_list
            total[task_id][section] = pruned_inner
    return total

def parse_args() -> argparse.Namespace:
    
    parser = argparse.ArgumentParser(description="Load input JSON and original dataset")
    parser.add_argument("--test_case_data_path", type=str, required=True, help="Path to test case data")
    parser.add_argument("--mode", type=str, required=True, help="Mode")
    parser.add_argument("--dataset", type=str, choices=["humaneval", "mbpp"], required=True, help="Dataset name to load originals from")
    parser.add_argument("--model_name", type=str, required=True, help="Model name")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save the dataset")
    return parser.parse_args()

def save_contract_test_cases(testcase_data, input_contract_test_case_list, output_path,mode):
    for task_id, value in input_contract_test_case_list.items():
        for contract_key, value2 in value.items():
            section = value2['section']
            case_index = value2['case_index']
            
            for test_case_instruction in value[contract_key]['test_case_instruction']:
                print(test_case_instruction)

    with open(f"{output_path}/{mode}.json", 'w') as f:
        json.dump(input_contract_test_case_list, f, indent=4)


if __name__ == "__main__":
    args = parse_args()
    print("="*100)
    print(f"**Start making code generation dataset -> {args.mode}, {args.dataset}, {args.model_name}**")
    print("="*100)
    # Load input JSON (e.g., contract check results)
    code_generation_data, testcase_data, original_data = load_dataset(args.dataset, args.test_case_data_path)

    # Make Code Generation Dataset
    created, input_contract_test_cases = code_generation_template_dataset(code_generation_data, testcase_data, original_data, args.mode, args.dataset)

    # Train-valid split
    train_rows, valid_rows = train_valid_split(created, 0.1)

    # Save jsonl
    save_jsonl(created, args.output_path, 'total') # total dataset
    print(f"✅ Successfully saved total dataset: {len(created)}")   
    save_jsonl(train_rows, args.output_path, 'train') # train dataset
    print(f"✅ Successfully saved train dataset: {len(train_rows)}")
    save_jsonl(valid_rows, args.output_path, 'valid') # valid dataset
    print(f"✅ Successfully saved valid dataset: {len(valid_rows)}")
    
    if args.mode == "CODE_GENERATION_CT":
        input_contract_test_case_list =[]
        for task_id, value in input_contract_test_cases.items():
            input_contract_test_case_list.append({task_id: value})    
        save_jsonl(input_contract_test_case_list, args.output_path, 'input_contract_test_cases') # input contract test cases
        save_json(input_contract_test_cases, args.output_path, 'input_contract_test_cases_check_format') # input contract test cases
        print(f"\n✅ Successfully saved input contract test cases: {len(input_contract_test_case_list)}")
        #save_contract_test_cases(testcase_data, input_contract_test_case_list, args.output_path, 'test_contract_test_case') # save contract test cases
        
        # Prune and save testcase_data by removing selected case_index per task_id/section
        pruned_testcase_data = prune_testcase_data(testcase_data, input_contract_test_cases)
        save_json(pruned_testcase_data, args.output_path, 'contract_check_results_pruned')
        print(f"✅ Successfully saved pruned contract_check_results: {len(pruned_testcase_data.keys())}")
        
        # Also save a version aligned to CT-selected tasks so counts match CT total
        aligned_to_ct = {task_id: pruned_testcase_data.get(task_id, {}) for task_id in input_contract_test_cases.keys()}
        save_json(aligned_to_ct, args.output_path, 'contract_check_results_pruned_aligned_to_ct')
        print(f"✅ Successfully saved pruned (aligned to CT tasks): {len(aligned_to_ct.keys())}")
        
    # Save TOTAL dataset: keep only AssertionError cases and deduplicate by case_index (aggregate contract_in_key)
    # This is used for evaluation
    total_assertion_only = assertion_only_dedup_testcase_data_gt(testcase_data, original_data, args.dataset)
    save_json(total_assertion_only, args.output_path, 'contract_check_results_total_assertion_only')
    print(f"✅ Successfully saved TOTAL assertion-only Checked dataset: {len(total_assertion_only.keys())}")
    
    print("\n✅ All code generation dataset saved.")
    print("="*100)