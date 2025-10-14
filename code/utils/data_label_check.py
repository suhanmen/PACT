import json
import pdb
import re
import textwrap
import ast
import math
import inspect
import multiprocessing
import os

"""
If you want to check the data label, you can use this script.

This script for HumanEval and Mbpp data.
"""

_docstring_re = re.compile(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', re.DOTALL)

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

def _strip_triple_quoted(src):
    return _docstring_re.sub('', src)

def canonical_solution_load_for_reward(dataset_tag, contracts_in="no_contracts"):
    if 'humaneval' in dataset_tag.lower():
        jsonl_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
    elif 'mbpp' in dataset_tag.lower():
        jsonl_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'

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
                if 'humaneval' in dataset_tag:
                    full_code = f"{prompt}\n{canonical_src}"
                else:
                    full_code = canonical_src

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


def functionality_test_case_data_load():
    humaneval_test_case_data = {}
    with open("../../data/evalplus-0.1.1/HumanEvalPlus.jsonl", "r") as f:
        for line in f:
            data = json.loads(line)
            humaneval_test_case_data[data["task_id"]] = data["plus_input"]
    
    mbpp_test_case_data = {}
    with open("../../data/mbppplus-0.2.0/MbppPlus.jsonl", "r") as f:
        for line in f:
            data = json.loads(line)
            mbpp_test_case_data[data["task_id"]] = data["plus_input"]
    
    return humaneval_test_case_data, mbpp_test_case_data

def contracts_test_case_data_load():
    humaneval_test_case_data = {}
    mbpp_test_case_data = {}
    
    with open("../../code/evaluation_test_case_pass_k/humaneval/pre_filtering/multi_assert_specification/o4-mini/o4-mini_all_results.json", "r") as f:
        data = json.load(f)
        for test_case in data:
            if test_case['task_id'] not in humaneval_test_case_data:
                humaneval_test_case_data[test_case['task_id']] = []
            try:
                if test_case['groundtruth_result'].startswith('AssertionError'):
                    humaneval_test_case_data[test_case['task_id']].append(test_case['input'])
            except:
                pass
    
    with open("../../code/evaluation_test_case_pass_k/mbpp/pre_filtering/multi_assert_specification/o4-mini/o4-mini_all_results.json", "r") as f:
        data = json.load(f)
        for test_case in data:
            if test_case['task_id'] not in mbpp_test_case_data:
                mbpp_test_case_data[test_case['task_id']] = []
            try:
                if test_case['groundtruth_result'].startswith('AssertionError'):
                    mbpp_test_case_data[test_case['task_id']].append(test_case['input'])
            except:
                pass
    
    return humaneval_test_case_data, mbpp_test_case_data

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

def run_func_with_timeout(func, args, timeout=5): 
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
        return run_func_with_timeout(func, args_to_pass, timeout=5)
    
    except AssertionError as e:
        #return f"AssertionError: {e}"
        return f"Exception: {e}"

    except Exception as e:
        return f"Exception: {e}"

def compute_functionality_score(dataset: dict, functionality_dataset: dict, tag: str):
    json_dict = {'Dataset_name': tag, 'Score': 0.0}
    total = 0
    passed = 0
    
    for task_id in dataset:
        generated_func = dataset[task_id][0]
        inputs = functionality_dataset[task_id]

        json_dict[task_id] = {'canonical_code': dataset[task_id][1], 
                              'entry_point': dataset[task_id][2],
                              'base_input': len(inputs),
                              'False_list':[]}

        for inp in inputs:

            #if task_id in ["Mbpp/106", "Mbpp/124", "Mbpp/580", "Mbpp/720"]:
            #    continue
            
            total += 1
            model_res = run_func_object(generated_func, inp)
            if isinstance(model_res, str):
                is_fail = model_res.startswith(("Exception", "TypeError", "Timeout", "InvalidInput"))
                if not is_fail:
                    passed += 1
                else:
                    json_dict[task_id]['False_list'].append('false')
            else:
                passed += 1
    
    json_dict['Score'] = (passed / total)*100
    os.makedirs(f"../../code/evaluation_data_check/functionality", exist_ok=True)
    with open(f"../../code/evaluation_data_check/functionality/{tag}.json", "w") as f:
        json.dump(json_dict, f, indent=2)
    
   
    return (passed / total)

def compute_contracts_score(dataset, contracts_dataset, tag):
    json_dict = {'Dataset_name': tag, 'Score': 0.0}
    total = 0
    passed = 0
    
    if tag == "Mbpp_in_contracts":
        task_id_list = contracts_dataset.keys()
    else:
        task_id_list = dataset.keys()
    
    for task_id in task_id_list:
            generated_func = dataset[task_id][0]
            inputs = contracts_dataset[task_id]
         
            json_dict[task_id] = {'canonical_code': dataset[task_id][1], 
                                'entry_point': dataset[task_id][2],
                                'base_input': len(inputs),
                                'False_list':[]}

            for inp in inputs:
                total += 1
                model_res = run_func_object(generated_func, inp)
                if isinstance(model_res, str):
                    is_AssertionError = model_res.startswith(("AssertionError"))
                    if is_AssertionError:
                        passed += 1
                    else:
                        json_dict[task_id]['False_list'].append('false')
                        pdb.set_trace()
    
    json_dict['Score'] = (passed / total)*100 
    os.makedirs(f"../../code/evaluation_data_check/contracts", exist_ok=True)
    with open(f"../../code/evaluation_data_check/contracts/{tag}.json", "w") as f:
        json.dump(json_dict, f, indent=2)
    
    return (passed / total)


if __name__ == "__main__":
    # load data
    humaneval_data_no_contracts = canonical_solution_load_for_reward("humaneval", contracts_in="no_contracts")
    humaneval_data_in_contracts = canonical_solution_load_for_reward("humaneval", contracts_in="in_contracts")
    mbpp_data_no_contracts = canonical_solution_load_for_reward("mbpp", contracts_in="no_contracts")
    mbpp_data_in_contracts = canonical_solution_load_for_reward("mbpp", contracts_in="in_contracts")
    
    # functionality dataset
    humaneval_test_case_data, mbpp_test_case_data = functionality_test_case_data_load()
    
    # Contracts dataset
    humaneval_contracts_data, mbpp_contracts_data = contracts_test_case_data_load()
    
    #Compute functionality score
    print("Compute functionality score")
    print("="*100)
    for tag, dataset in [("HumanEval_no_contracts", humaneval_data_no_contracts), ("HumanEval_in_contracts", humaneval_data_in_contracts)]:
        functionality_score = compute_functionality_score(dataset, humaneval_test_case_data,tag)
        print(f"Dataset: {tag}")
        print(f"Functionality score for : {functionality_score*100}")
    print("="*100)
    
    for tag, dataset in [("Mbpp_no_contracts", mbpp_data_no_contracts), ("Mbpp_in_contracts", mbpp_data_in_contracts)]:
        functionality_score = compute_functionality_score(dataset, mbpp_test_case_data,tag)
        print(f"Dataset: {tag}")
        print(f"Functionality score for : {functionality_score*100}")
    print("="*100)
    
    # Compute Contracts score
    print("\n\nCompute contracts score")
    print("="*100)
    for tag, dataset, contract_dataset in [("HumanEval_in_contracts", humaneval_data_in_contracts, humaneval_contracts_data), ("Mbpp_in_contracts", mbpp_data_in_contracts, mbpp_contracts_data)]:
        contracts_score = compute_contracts_score(dataset, contract_dataset, tag)
        print(f"Dataset: {tag}")
        print(f"Contracts score for : {contracts_score*100}")
    print("="*100)
