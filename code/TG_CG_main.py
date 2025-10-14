import os
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import Adam
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    PreTrainedTokenizerBase,
)
from peft import get_peft_model
import pdb
from tqdm import tqdm
from typing import List, Union, Dict
import json
import re
import codecs
import time
from pathlib import Path
from itertools import islice
import textwrap
import warnings
import inspect
import types
from typing import Any
from utils.Instruction import instruction_template
from utils.model_setting import bnb_config, lora_config
from utils.evaluation_test_case_pass_k import safe_eval, run_func_with_timeout


# Global counters copied from code_generation_main semantics (for logging/test-case filtering)
func_filtered_task_id = []
func_total_test_case = 0
func_filtered_test_case = 0
conc_total_test_case = 0
conc_filtered_test_case = 0

# if you want to add new model, you need to add it here
def simple_model_name(model_name):
    if model_name == "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B":
        return "DeepSeek"
    elif model_name == "mistralai/Mistral-Nemo-Base-2407":
        return "Mistral"
    elif model_name == "Qwen/Qwen3-14B":
        return "Qwen"
    elif model_name == "microsoft/Phi-4-reasoning-plus":
        return "Phi"
    elif model_name == "microsoft/Phi-4-reasoning":
        return "Phi-reasoning"
    
def load_jsonl_to_dict(jsonl_path, original_path=None, total_jsonl_path=None, use_instruction='None'):
    task_map = {}
    original_data = {}
    total_data_task_id = {}
    
    # for original data : contract, entry_point
    if original_path:
        with open(original_path, 'r', encoding='utf-8') as f:
            for line in f:
                item = json.loads(line)
                task_id = item['task_id']
                original_data[task_id] = {
                    'contract': item.get('contract'),
                    'entry_point': item.get('entry_point', 'solution')
                }

    # total task_id
    if total_jsonl_path:
        with open(total_jsonl_path, 'r', encoding='utf-8') as f:
            for line in f:
                item = json.loads(line)
                task_id = item['name']
                total_data_task_id[task_id] = item
    
    # code promt data
    try:
        with open(jsonl_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    i = json.loads(line)
                except:
                    if "\\zn" in line:
                        line = line.replace("\\zn", "\\n")
                    i = json.loads(line)
                
                
                if "CODE_GENERATION_CS" in use_instruction:
                    task_id = i['name']
                    task_map[task_id] = {
                        'prompt': i['grammar'][0]['production'][0],
                        'contract': original_data[task_id]['contract'],
                        'entry_point': original_data[task_id]['entry_point'],
                    }
                
                elif "CODE_GENERATION_CT" in use_instruction:
                    # not use full data.
                    if total_data_task_id != {}:
                        if i['name'] not in total_data_task_id.keys():
                            continue
                    
                    task_id = i['name']
                    task_map[task_id] = {
                        'contract':original_data[task_id]['contract'],
                        'entry_point':original_data[task_id]['entry_point'],
                        'system': i['description'][0]['content'],
                        'user': i['description'][1]['content'],
                        }
                
                # elif use_instruction == "CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CS":
                #     task_id = i['name']
                #     task_map[task_id] = {
                #         'contracts': i['grammar'][0]['constraints'],
                #         'contracts_natural_language': i['grammar'][0]['production'][0],
                #         'contracts_json': i['grammar'][0]['production'][1],
                #     }
                    
                # elif use_instruction == "CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CT":
                #     task_id = i['name']
                #     task_map[task_id] = {
                #         'contracts': i['grammar'][0]['constraints'],
                #         'contracts_test_case': i['grammar'][0]['production'][0],
                #     }
                
                else:
                    task_id = i['task_id']
                    task_map[task_id] = {
                        'prompt': i['prompt'],
                        'contract': i['contract'],
                        'canonical_solution': i['canonical_solution'],
                        'entry_point': i.get('entry_point', 'solution'),
                    }
        
    except Exception as e:
        print(e)
        pdb.set_trace()
    return task_map

def python_like_to_json(text):
    text = text.replace("True", "true").replace("False", "false").replace("None", "null")
    text = re.sub(r"\(([^()]*?,[^()]*?)\)", r"[\1]", text)
    return text

def extract_output_json(text):
    if isinstance(text, list):
        text = text[0]

    if text.strip().startswith("```json"):
        match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
        if match:
            text = match.group(1)
            
    text = re.split(r"(</div>|<script|\n---|\n```|\n#)", text)[0].strip()
    text = python_like_to_json(text)

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        return None

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def _build_contract_str(contracts: Union[str, List, Dict]) -> str:
    if not contracts:
        return ""

    if isinstance(contracts, list):
        flat = []
        for item in contracts:
            if isinstance(item, dict):
                flat.extend(item.values())
            else:
                flat.append(str(item))
        contracts = "\n".join(flat)

    if isinstance(contracts, dict):
        def key_order(k): 
            m = re.search(r"\d+", k)
            return int(m.group()) if m else k
        lines = [contracts[k] for k in sorted(contracts, key=key_order)]

    else:
        lines = []
        try:
            obj = json.loads(contracts)
            if isinstance(obj, dict):
                lines = [obj[k] for k in sorted(obj)]
        except json.JSONDecodeError:
            pass
        
        if not lines:
            lines = contracts.splitlines()

    cleaned = []
    for raw in lines:
        raw = str(raw).strip()
        if not raw:
            continue
        if re.match(r"^(contract list|canonical solution):?", raw, re.I):
            continue
        if raw.startswith("assert_") and ":" in raw:
            raw = raw.split(":", 1)[1].strip()
        raw = raw.replace("# $_CONTRACT_$", "").strip(" ,\"")
        if not raw.startswith("assert "):
            continue
        cleaned.append(raw)

    return "\n".join(f"assert_{i}: {c}" for i, c in enumerate(cleaned)) + ("\n" if cleaned else "")


def ensure_chat_template(tok):
    if getattr(tok, "chat_template", None):
        return

    name = tok.name_or_path.lower()
    
    if "mistral" in name or "mixtral" in name:
        tok.chat_template = (
            "{% for m in messages %}"
            "{% if m['role'] == 'user' %}[INST] {{ m['content'] }} [/INST]\n"
            "{% elif m['role'] == 'assistant' %}{{ m['content'] }}\n"
            "{% elif m['role'] == 'system' %}{{ m['content'] }}\n"
            "{% else %}{{ m['content'] }}\n{% endif %}"
            "{% endfor %}"
            "{% if add_generation_prompt %}{% endif %}"
        )
        return

    tok.chat_template = (
        "{% for m in messages %}"
        "{{ m['role'] | capitalize }}: {{ m['content'] }}\n"
        "{% endfor %}"
        "{% if add_generation_prompt %}Assistant: {% endif %}"
    )


def safe_extract_json(text):
    if isinstance(text, list):
        if not text:
            return None
        text = text[0]

    m = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", text, re.DOTALL)
    if not m:
        return None

    try:
        json_blob = m.group(1) if isinstance(m, re.Match) else m.group(0)
        json_blob = python_like_to_json(json_blob)
        obj = json.loads(json_blob)
    except json.JSONDecodeError:
        return None

    if isinstance(obj, dict) and "code" in obj:
        code_str = obj["code"]
        code_str = codecs.decode(code_str, "unicode_escape")
        return code_str.strip("\n")

    return obj

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

def test_case_template_dataset(task_id, dataset, INSTRUCTION, entry, desc, sol, tests, OUTPUT_INSTRUCTION, tokenizer, use_instruction=None, contracts=None):
    system, user = "", ""
    contract_str = _build_contract_str(contracts) if contracts else ""
    system = f"{INSTRUCTION}\n\n"
    
    if dataset == "humaneval":
        sol_with_contracts = sol
    elif dataset == "mbpp":
        sol_with_contracts = _inject_contracts_into_solution(sol, contracts, entry)
    
    if dataset == "humaneval":
        i_user = (
            f"Method Name: {entry}\n"
            f"Problem Description:\n{desc}\n"
            f"{contracts}"
            f"{sol}\n\n"
            f"Contract List:\n{contract_str}\n"
        )
    elif dataset == "mbpp":
        i_user = (
                f"Method Name: {entry}\n"
                f"Problem Description:\n{desc}\n"
                f"{sol_with_contracts}\n\n"
                f"Contract List:\n{contract_str}\n"
        )        
        
    # Type 1
    user = OUTPUT_INSTRUCTION + i_user
    
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    
    # Type 2
    #messages = [{"role": "system", "content": system + OUTPUT_INSTRUCTION}, {"role": "user", "content": i_user}]
    
    # Type 3
    #messages = [{"role": "user", "content": system + user}]
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)                      

def code_generation_template_dataset(task_id, dataset, example, INSTRUCTION, entry, desc, sol, tests, OUTPUT_INSTRUCTION, tokenizer, use_instruction=None, contracts=None, model_base_name=None, code_gen_mode='SFT'):
    global func_total_test_case, func_filtered_test_case, conc_total_test_case, conc_filtered_test_case
    messages = [{"role": "user", "content": ""}]
    user = ""
    data_path_base=f"../../code/evaluation_test_case_pass_k/{dataset}/pre_filtering"
    combined_model_name = f"{code_gen_mode}-{simple_model_name(model_base_name[0])}"
##################################################################################################
    if "CODE_GENERATION" in use_instruction:
        if use_instruction == "CODE_GENERATION_CS":
            user = (
                f"{example['system']}\n"
                f"{example['user']}"
            )
            # user = (
            #     f"{INSTRUCTION}\n\n"
            #     f"Method Name: {entry}\n"
            #     f"Problem Description:\n{desc}\n"
            #     f"{OUTPUT_INSTRUCTION}"
            # )
        elif use_instruction == "CODE_GENERATION_CT":
            user = (
                f"{example['system']}\n"
                f"{example['user']}"
            )
            # # functionality_test_cases = ""
            # # contract_test_cases = ""
            
            # # if dataset == "humaneval":
            # #     func_data_path = f"{data_path_base}/functionality_specification/{combined_model_name}/{combined_model_name}_pre_filtering_functionality_results_filtered.json"
            # #     conc_data_path = f"{data_path_base}/assert_specification/{combined_model_name}/{combined_model_name}_pre_filtering_contracts_results_filtered.json"
            # #     sol_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
            # #     original_data_dict = load_jsonl_to_dict(sol_path, use_instruction='dummy')
            # #     play_sol_with_contracts = original_data_dict[task_id]["prompt"] + "\n" + original_data_dict[task_id]["canonical_solution"]
                
                
            # # elif dataset == 'mbpp':
            # #     func_data_path = f"{data_path_base}/functionality_specification/{combined_model_name}/{combined_model_name}_pre_filtering_functionality_results_filtered.json"
            # #     conc_data_path = f"{data_path_base}/assert_specification/{combined_model_name}/{combined_model_name}_pre_filtering_contracts_results_filtered.json"
            # #     sol_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
            # #     original_data_dict = load_jsonl_to_dict(sol_path, use_instruction='dummy')
            # #     play_sol_with_contracts = original_data_dict[task_id]["prompt"] + "\n" + original_data_dict[task_id]["canonical_solution"]
            
            # # load sol
            # ns: dict[str, Any] = {}

            # exec(compile(play_sol_with_contracts, "<contract_src>", "exec"), ns)
            # fn: types.FunctionType = ns[entry]
            # param_cnt = len(inspect.signature(fn).parameters)
            
            # with open(func_data_path, "r") as st_json:
            #     func_data_dict = json.load(st_json)
            # with open(conc_data_path, "r") as st_json:
            #     conc_data_dict = json.load(st_json)
            
            # func_dataset_name = list(func_data_dict.keys())[0]
            # conc_dataset_name = list(conc_data_dict.keys())[0]
            # try:
            #     for func_key in func_data_dict[func_dataset_name][task_id]:
            #         functionality_test_cases += f'{func_key}:\n'
            #         for values in func_data_dict[func_dataset_name][task_id][func_key]:
            #             for _,value in values.items():
            #                 value = safe_eval(value)
            #                 if param_cnt == 1:
            #                     if isinstance(value, (list, tuple)) and len(value) == 1:
            #                         args_to_pass = [value[0]]
            #                     else:
            #                         args_to_pass = [value]
            #                 else:
            #                     args_to_pass = value if isinstance(value,(list,tuple)) else [value]
            #                 str_args_to_pass = ', '.join(repr(i) if isinstance(i, str) else str(i) for i in args_to_pass)

            #                 if len(str_args_to_pass) > 10000:
            #                     func_filtered_test_case += 1
            #                     func_filtered_task_id.append(task_id)
            #                 else:
            #                     result = run_func_with_timeout(fn, args_to_pass)
            #                     formatted_result = repr(result) if isinstance(result, str) else str(result)
            #                     functionality_test_cases += f'>>> {entry}({str_args_to_pass})\n {formatted_result}\n'                     
            #                 func_total_test_case += 1
            #         functionality_test_cases += '\n'

            # except:
            #     functionality_test_cases = f"None\n"    
            
            
            
            # try:
            #     for assert_key in conc_data_dict[conc_dataset_name][task_id]:
            #         contract_test_cases += f'{assert_key}:\n'
            #         for values in conc_data_dict[conc_dataset_name][task_id][assert_key]:
            #             for _,value in values.items():
            #                 value = safe_eval(value)
            #                 if param_cnt == 1:
            #                     if isinstance(value, (list, tuple)) and len(value) == 1:
            #                         args_to_pass = [value[0]]
            #                     else:
            #                         args_to_pass = [value]
            #                 else:
            #                     args_to_pass = value if isinstance(value,(list,tuple)) else [value]
            #                 args_to_pass = ', '.join(repr(i) if isinstance(i, str) else str(i) for i in args_to_pass)
            #                 if len(args_to_pass) > 10000:
            #                     conc_filtered_test_case += 1 
            #                 else:
            #                     contract_test_cases += f'>>> {entry}({args_to_pass})\n "AssertionError: invalid input"\n'                     
            #                 conc_total_test_case += 1
            #         contract_test_cases += '\n'
            # except:
            #     contract_test_cases = None
            # user = (
            #     f"{INSTRUCTION}\n\n"
            #     f"Method Name: {entry}\n"
            #     f"Problem Description:\n{desc}\n"
            #     f"{OUTPUT_INSTRUCTION}"
            #     f"Functionality Test Cases:\n{functionality_test_cases}\n"
            #     f"Contract Test Cases:\n{contract_test_cases}\n"
            # )
##################################################################################################                
    # elif "CODE_REFINEMENT_WITH_INSTRUCTIONS" in use_instruction:
    #     system = f"{INSTRUCTION}\n\n"
    #     base_data_path = "../../code/output_gpt/original/gpt-4o-mini/CONTRACTS_INDIVIDUAL"
    #     if use_instruction == "CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CS":
    #         if dataset == "humaneval":
    #             data_path = f"{base_data_path}/humaneval_gpt-4o-mini_sft.jsonl"
    #             sol_with_contracts = sol
    #         elif dataset == 'mbpp':
    #             data_path = f"{base_data_path}/mbpp_gpt-4o-mini_sft.jsonl"
    #             sol_with_contracts = _inject_contracts_into_solution(sol, contracts, entry)
            
    #         data_dict = load_jsonl_to_dict(data_path, use_instruction=use_instruction)
    #         dict_constraints = data_dict[task_id]["contracts_json"]
    #         natural_language_constraints = ""
    #         for i, (key, value) in enumerate(dict_constraints.items()):
    #             natural_language_constraints += f"\n{i}: {value}"
            
    #         user = (
    #             f"{INSTRUCTION}\n\n"
    #             f"Method Name: {entry}\n"
    #             f"Problem Description:\n{desc}\n"
    #             f"{sol_with_contracts}\n\n"
    #             f"Constraints:\n{natural_language_constraints}\n"
    #             f"{OUTPUT_INSTRUCTION}"
    #         ) 
    #     elif use_instruction == "CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CT":
    #         contract_test_case = ""
    #         if dataset == "humaneval":
    #             data_path = f"{data_path_base}/assert_specification/{combined_model_name}/{combined_model_name}_pre_filtering_contracts_results_filtered.json"
    #             sol_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
    #             original_data_dict = load_jsonl_to_dict(sol_path, use_instruction='dummy')
    #             sol_with_contracts = original_data_dict[task_id]["prompt"] + "\n" + original_data_dict[task_id]["canonical_solution"]
    #         elif dataset == 'mbpp':
    #             data_path = f"{data_path_base}/assert_specification/{combined_model_name}/{combined_model_name}_pre_filtering_contracts_results_filtered.json"
    #             sol_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
    #             original_data_dict = load_jsonl_to_dict(sol_path, use_instruction='dummy')
    #             sol_with_contracts = original_data_dict[task_id]["canonical_solution"]

    #         ns: dict[str, Any] = {}
            
    #         exec(compile(sol_with_contracts, "<contract_src>", "exec"), ns)
    #         fn: types.FunctionType = ns[entry]
    #         param_cnt = len(inspect.signature(fn).parameters)
            
    #         with open(data_path, "r") as st_json:
    #             data_dict = json.load(st_json)
            
    #         dataset_name = list(data_dict.keys())[0]
    #         try:
    #             for assert_key in data_dict[dataset_name][task_id]:
    #                 contract_test_case += f'{assert_key}:\n'
    #                 for values in data_dict[dataset_name][task_id][assert_key]:
    #                     for _,value in values.items():
    #                         value = safe_eval(value)
    #                         if param_cnt == 1:
    #                             if isinstance(value, (list, tuple)) and len(value) == 1:
    #                                 args_to_pass = [value[0]]
    #                             else:
    #                                 args_to_pass = [value]
    #                         else:
    #                             args_to_pass = value if isinstance(value,(list,tuple)) else [value]
    #                         args_to_pass = ', '.join(repr(i) if isinstance(i, str) else str(i) for i in args_to_pass)

    #                         contract_test_case += f'>>> {entry}({args_to_pass})\n "AssertionError: invalid input"\n'                     
    #                 contract_test_case += '\n'
    #         except:
    #             contract_test_case = None
            
    #         if contract_test_case:
    #             user = (
    #                 f"{INSTRUCTION}\n\n"
    #                 f"Method Name: {entry}\n"
    #                 f"Problem Description:\n{original_data_dict[task_id]['prompt']}\n"
    #                 f"{original_data_dict[task_id]['canonical_solution']}\n\n"
    #                 f"Constraints test case:\n{contract_test_case}\n"
    #                 f"{OUTPUT_INSTRUCTION}"
    #             )
    #         else:
    #             user = 'None'
    
    if user == 'None':
        encoded = 'None'
    else:
        messages[0]["content"] = user
        
        ## if you want chat template
        encoded = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        
        ## not chat template
        # data not in cot
        encoded = encoded + "I have done a short CoT reasoning and Aha! I have found the right answer.\n</think>\n\n```"
        
        # data in cot
        #encoded = encoded + example['reasoning'][0]
    return encoded

def build_prompt(dataset, task_id, example, tokenizer, use_instruction, model_base_name, code_gen_mode):
    entry = example.get('entry_point', '')
    desc  = example.get('prompt', '')
    sol   = example.get('canonical_solution', '')
    tests = example.get('test', [])
    contracts = example.get('contract', '')
    instruction, output_instruction = instruction_template(use_instruction)
    ensure_chat_template(tokenizer)     

    if use_instruction in ["CODE_GENERATION_CS", "CODE_GENERATION_CT", "MAKE_CODE_BLOCK_FS_CS", "MAKE_CODE_BLOCK_FT_CT", "CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CS", "CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CT"]:
        return code_generation_template_dataset(task_id, dataset, example, instruction, entry, desc, sol, tests, output_instruction, tokenizer, use_instruction, contracts, model_base_name, code_gen_mode)
    else:
        return test_case_template_dataset(task_id, dataset, instruction, entry, desc, sol, tests, output_instruction, tokenizer, use_instruction, contracts)
    
def count_output_tokens_only(tokenizer: PreTrainedTokenizerBase, input_prompt: str, outputs: List[str]) -> int:
    total = 0
    for out in outputs:
        out_ids = tokenizer(out, add_special_tokens=False)["input_ids"]
        total += len(out_ids)
    return total

def init_dict(model_key, args_settings):
    return {'Setting': args_settings, model_key: []}

def load_dataset(args):
    if args.dataset == "humaneval" and "CODE_GENERATION_CS" == args.use_instruction :
        jsonl_path = '../../code/output_gpt/original/gpt-4o-mini/code_generation/humaneval_gpt-4o-mini_sft.jsonl'
        total_jsonl_path = '../../data/code_generation/total/CODE_GENERATION_CS/o4-mini/total.jsonl'
        original_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
        train_dataset = load_jsonl_to_dict(jsonl_path, original_path, None,args.use_instruction)
    elif args.dataset == "mbpp" and "CODE_GENERATION_CS" == args.use_instruction:
        jsonl_path = '../../code/output_gpt/original/gpt-4o-mini/code_generation/mbpp_gpt-4o-mini_sft.jsonl'
        total_jsonl_path = '../../data/code_generation/total/CODE_GENERATION_CS/o4-mini/test.jsonl'
        original_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
        train_dataset = load_jsonl_to_dict(jsonl_path, original_path, None,args.use_instruction)       
    
    elif args.dataset == "humaneval" and "CODE_GENERATION_CT" == args.use_instruction:
        jsonl_path = f'../../data/code_generation/{args.dataset}/{args.use_instruction}/o4-mini/total.jsonl'
        total_jsonl_path = f'../../data/code_generation/total/{args.use_instruction}/o4-mini/total.jsonl'
        original_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
        train_dataset = load_jsonl_to_dict(jsonl_path, original_path, total_jsonl_path,args.use_instruction)
    elif args.dataset == "mbpp" and "CODE_GENERATION_CT" == args.use_instruction:
        jsonl_path = f'../../data/code_generation/{args.dataset}/{args.use_instruction}/o4-mini/total.jsonl'
        total_jsonl_path = f'../../data/code_generation/total/{args.use_instruction}/o4-mini/total.jsonl'
        original_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
        train_dataset = load_jsonl_to_dict(jsonl_path, original_path, total_jsonl_path,args.use_instruction)
    
    # TOTAL DATASET
    elif args.dataset == "total":
        train_dataset = {}
        with open(f'../../data/code_generation/total/{args.use_instruction}/o4-mini/total.jsonl', 'r', encoding='utf-8') as f:
            for line in f:
                item = json.loads(line)
                task_id = item['name']
                train_dataset[task_id] = {
                    'system': item['description'][0]['content'],
                    'user': item['description'][1]['content'],
                    'contract': item['grammar'][0]['constraints'],
                    'reasoning': item['reasoning'],
                }
                
    elif args.dataset == 'humaneval':
        jsonl_path = '../../data/evalplus-0.1.1/HumanEvalPlus.jsonl'
        train_dataset = load_jsonl_to_dict(jsonl_path)
    elif args.dataset == 'mbpp':
        jsonl_path = '../../data/mbppplus-0.2.0/MbppPlus.jsonl'
        train_dataset = load_jsonl_to_dict(jsonl_path)
    
    return train_dataset

def _read_existing_single(save_path, model_key):
    '''
    This function reads the existing data from the save_path and returns a dictionary of task_ids that have been completed.
    '''
    if not os.path.exists(save_path):
        return {}, set()
    try:
        with open(save_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {}, set()

    done = set()
    for rec in data.get(model_key, []):
        tid = rec.get("task_id")
        if isinstance(tid, list):
            done.update(tid)
        elif tid is not None:
            done.add(tid)
    return data, done

def special_token_for_only_output(model_name):
    if model_name == "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B":
        return "<\uff5cAssistant\uff5c><think>\n"
    elif model_name == "mistralai/Mistral-Nemo-Base-2407":
        return "<|im_start|>assistant\n"
    elif model_name == "Qwen/Qwen3-14B":
        return "\nassistant\n<think>\n"
    elif model_name == "microsoft/Phi-4-reasoning-plus":
        return "assistant<think>"
    elif model_name == "microsoft/Phi-4-reasoning":
        return "assistant<think>"
    else:
        warnings.warn(f"Special token for only output is not defined for {model_name}")
        pdb.set_trace()
        return None

# ====== Model Classes ======
class Trainer:
    def __init__(self, model_names, max_length, max_new_tokens, use_qlora=False):
        model_name = model_names[0]
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_names[0], trust_remote_code=True)
        self.tokenizer.padding_side = "left"
        if self.tokenizer.pad_token_id is None or isinstance(self.tokenizer.pad_token_id, list):
            eos_id = self.tokenizer.eos_token_id
            if isinstance(eos_id, list):
                eos_id = eos_id[0]
            self.tokenizer.pad_token = self.tokenizer.convert_ids_to_tokens(eos_id)
            self.tokenizer.pad_token_id = eos_id
            
        if use_qlora:
            base = AutoModelForCausalLM.from_pretrained(
                model_name,
                quantization_config=bnb_config,
                device_map="auto",
                trust_remote_code=True
            )
            model = get_peft_model(base, lora_config)
        else:
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                dtype=torch.float16,
                device_map="auto",
                trust_remote_code=True
            )

        eos_id = model.config.eos_token_id
        if isinstance(eos_id, list):
            eos_id = eos_id[0]
        pad_id = model.config.pad_token_id or eos_id
        if isinstance(pad_id, list):
            pad_id = eos_id

        model.config.pad_token_id = pad_id
        model.config.eos_token_id = eos_id
        model.config.use_cache = False

        self.models = {model_name: model}
        
        self.max_length = int(max_length)
        
        if max_new_tokens != 0:
            self.max_new_tokens = int(max_new_tokens)
        else:
            self.max_new_tokens = -1

    

    @torch.no_grad()
    def _generate_batch(self, model, prompts, n=1):
        dev = next(model.parameters()).device

        inputs = self.tokenizer(
            prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=self.max_length
        ).to(dev)

        input_length = inputs.input_ids.shape[1]
        available_tokens = self.max_length - input_length
        actual_max_new_tokens = self.max_new_tokens if self.max_new_tokens != -1 else available_tokens

        outputs_list, full_outputs_list = [], []
        for _ in range(n):
            g = model.generate(
                input_ids=inputs.input_ids,
                attention_mask=inputs.attention_mask,
                pad_token_id=model.config.pad_token_id,
                eos_token_id=model.config.eos_token_id,
                do_sample=False, # True
                temperature=1.0, # 1.0
                top_k=None, # 50
                top_p=None, # 0.95
                max_new_tokens=actual_max_new_tokens,
                use_cache=True # default False
            )

            batch_texts = self.tokenizer.batch_decode(g, skip_special_tokens=True) # default False

            for idx, full_text in enumerate(batch_texts):
                special_token = special_token_for_only_output(model.config._name_or_path)
                if special_token in full_text:
                    gen_text = full_text.split(special_token)[-1].strip()
                else:
                    prompt_len = len(self.tokenizer(prompts[idx], add_special_tokens=False)["input_ids"])
                    gen_text = full_text[prompt_len:]

                outputs_list.append(gen_text.strip())
                full_outputs_list.append(full_text)

        return outputs_list, full_outputs_list
    
    # def _generate_single(self, model, prompt, n=1):
    #     dev = next(model.parameters()).device
    #     inputs = self.tokenizer(
    #         prompt, 
    #         return_tensors="pt",
    #         padding=True, 
    #         truncation=True,
    #         max_length=self.max_length).to(dev)
        
    #     # Calculate available tokens for generation
    #     input_length = inputs.input_ids.shape[1]
    #     available_tokens = self.max_length - input_length
    #     # Use the smaller of: available_tokens or self.max_new_tokens
    #     if self.max_new_tokens != -1:
    #         actual_max_new_tokens = self.max_new_tokens
    #     else:
    #         actual_max_new_tokens = available_tokens
        
    #     outputs_list, full_outputs_list = [], []
    #     for _ in range(n):
    #         g = model.generate(
    #             input_ids=inputs.input_ids,
    #             attention_mask=inputs.attention_mask,
    #             pad_token_id=model.config.pad_token_id,
    #             eos_token_id=model.config.eos_token_id,
    #             do_sample=True,
    #             temperature=1.0,
    #             top_k=50,
    #             top_p=0.95,
    #             max_new_tokens=actual_max_new_tokens,
    #             use_cache=False
    #         )
            
    #         full_text = self.tokenizer.decode(g[0], skip_special_tokens=False)
    #         model_id = getattr(model.config, "_name_or_path", None)
    #         special_token = special_token_for_only_output(model_id)
            
    #         # Debugging for token
    #         if special_token in full_text:
    #             gen_text = full_text.split(special_token)[-1].strip()
    #         else:
    #             prompt_len = inputs.input_ids.shape[1]
    #             gen_text = full_text[prompt_len:]
            
    #         outputs_list.append(gen_text.strip())
    #         full_outputs_list.append(full_text)
    #     return outputs_list, full_outputs_list

    def generate_responses(self, prompts, idx, contracts, n=1, skip_map=None):
        results = {Path(name).name: [] for name in self.models.keys()}
        for model_name, model in self.models.items():
            short_name = Path(model_name).name
            skip_ids = skip_map.get(short_name, set()) if skip_map else set()
            outputs, full_outputs = self._generate_batch(model, prompts, n)

            for tid, prompt, c, out, full_out in zip(idx, prompts, contracts, outputs, full_outputs):
                if tid in skip_ids:
                    continue

                input_tokens = len(self.tokenizer(prompt, add_special_tokens=False)["input_ids"])
                token_count = count_output_tokens_only(self.tokenizer, prompt, [out])
                contracts_str = _build_contract_str(c) if c else ""

                contract_dict = {}
                for line in contracts_str.splitlines():
                    if ":" in line:
                        key, val = line.split(":", 1)
                        contract_dict[key.strip()] = val.strip()

                results[short_name].append({
                    "task_id": tid,
                    "input": prompt,
                    "outputs": [out],
                    "full_outputs": [full_out],
                    "contracts": c,
                    "contracts_list": contract_dict,
                    "input_tokens": input_tokens,
                    "output_tokens": token_count
                })
        return results

    # def generate_responses(self, prompts, idx, contracts, n=1, skip_map=None):
    #     results = {Path(name).name: [] for name in self.models.keys()}
    #     for model_name, model in self.models.items():
    #         short_name = Path(model_name).name
    #         skip_ids = skip_map.get(short_name, set()) if skip_map else set()

    #         for tid, prompt, c in zip(idx, prompts, contracts):
    #             if tid in skip_ids:
    #                 continue

    #             input_tokens = len(self.tokenizer(prompt, add_special_tokens=False)["input_ids"])
    #             outputs, full_outputs = self._generate_single(model, prompt, n)
    #             token_count = count_output_tokens_only(self.tokenizer, prompt, outputs)
    #             contracts_str = _build_contract_str(c) if c else ""

    #             contract_dict = {}
    #             for line in contracts_str.splitlines():
    #                 if ":" in line:
    #                     key, val = line.split(":", 1)
    #                     contract_dict[key.strip()] = val.strip()

    #             results[short_name].append({
    #                 "task_id": tid,
    #                 "input": prompt,
    #                 "outputs": outputs,
    #                 #"parsed_outputs": [safe_extract_json(o) for o in outputs],
    #                 "full_outputs": full_outputs,
    #                 "contracts": c,
    #                 "contracts_list": contract_dict,
    #                 "input_tokens": input_tokens,
    #                 "output_tokens": token_count
    #             })
    #     return results

def input_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default="humaneval")
    parser.add_argument("--model_name", nargs='+', type=str, required=True)
    parser.add_argument("--batch_size", type=int, default=4, help="Number of prompts to process per training step (i.e., batch size of tasks)")
    parser.add_argument("--num_samples", type=int, default=4, help="Number of outputs to generate per prompt per agent")
    parser.add_argument("--max_length", type=int, default=4096, help="Maximum number of input")
    parser.add_argument("--max_new_tokens", type=int, default=2048, help="Maximum number of new tokens to generate")
    parser.add_argument("--use_instruction", type=str, help="Include instruction in prompt if set.")
    parser.add_argument("--use_qlora", type=lambda x: x.lower() == "true", default=False)
    parser.add_argument("--skip_completed", type=lambda x: x.lower() == "true", default=True, help="Skip completed task_ids (True/False)")
    parser.add_argument("--code_gen_mode", type=str, default=None, help="Code generation mode")
    parser.add_argument("--sample_n", type=lambda x: x.lower() == "true", default=False, help="Sample n test cases (True/False)")
    return parser.parse_args()

def all_root(args):
    pwd = Path.cwd()
    model_name = Path(args.model_name[0]).name  
    base_dir   = Path("../../code/output_base") / args.dataset / "inference"

    special_map = {
        # code generation styles
        "CODE_GENERATION_CS": "code_generation_cs",
        "CODE_GENERATION_CT": "code_generation_ct",
        #"MAKE_CODE_BLOCK_FS_CS": "make_code_block_fs_cs",
        #"MAKE_CODE_BLOCK_FT_CT": "make_code_block_ft_ct",
        #"CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CS": "code_refinement_with_instructions_fc_cs",
        #"CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CT": "code_refinement_with_instructions_fc_ct",
        
        # test-case styles (kept for compatibility)
        "ASSERT_SPECIFICATION": "assert_specification",
        "FUNCTIONALITY_SPECIFICATION": "functionality_specification",
        
        "MULTI_ASSERT_SPECIFICATION": "multi_assert_specification",
        "MULTI_ASSERT_SPECIFICATION_humaneval": "multi_assert_specification_humaneval",
        "MULTI_ASSERT_SPECIFICATION_mbpp": "multi_assert_specification_mbpp",
        
        "GRAMMAR_ASSERT_SPECIFICATION": "grammar_assert_specification",
        "GRAMMAR_ASSERT_SPECIFICATION_humaneval": "grammar_assert_specification_humaneval",
        "GRAMMAR_ASSERT_SPECIFICATION_mbpp": "grammar_assert_specification_mbpp",
    }

    
    
    if args.dataset == "total":
        output_dir = Path("../../code/output_full/total/inference") / model_name / args.use_instruction.lower()
    else:
        subfolder = special_map.get(args.use_instruction)
        output_dir = base_dir / subfolder / model_name
    
    output_dir.mkdir(parents=True, exist_ok=True)

    filenames = {"generate": "generated_step_all.json",}
    save_root = output_dir / filenames["generate"]
    return str(pwd), str(output_dir), save_root

def single_toggles(contracts_dict):
    single_toggles = []
    for key in contracts_dict.keys():
        single_toggles.append({"id": key, "on": f"({contracts_dict[key]})", "off": f"({contracts_dict[key]})"})
    return single_toggles


if __name__ == "__main__":
    args = input_parser()
    pwd, output_dir, save_root = all_root(args)
    os.makedirs(output_dir, exist_ok=True)
    
    trainer = Trainer(args.model_name, args.max_length, args.max_new_tokens, use_qlora=args.use_qlora)
    train_dataset = load_dataset(args)
    task_ids       = list(train_dataset.keys())
    prompts    = {
        tid: build_prompt(
                args.dataset, 
                tid, 
                example, 
                trainer.tokenizer,
                args.use_instruction, 
                model_base_name=args.model_name,
                code_gen_mode=args.code_gen_mode
            )
        for tid, example in train_dataset.items()
    }
    contracts_map = {tid: example["contract"] for tid, example in train_dataset.items()}
    
    for tid in task_ids[:10]:
        print(tid)
        print(prompts[tid])
        print('--------------------------------')
        print('--------------------------------')

    # For test
    if args.sample_n:
        SAMPLE_N = 5
        prompts  = dict(islice(prompts.items(), SAMPLE_N))
        contracts_map = {tid: contracts_map[tid] for tid in prompts}
        task_ids = list(prompts.keys())  
    
    model_key = args.model_name[0].split("/")[1]

    if args.skip_completed:
        all_generated, completed_ids = _read_existing_single(save_root, model_key)
        if not all_generated:
            all_generated = init_dict(model_key, vars(args))
    else:
        all_generated = init_dict(model_key, vars(args))
        completed_ids = set()

    all_generated.setdefault(model_key, [])
    all_generated.setdefault("Setting", {})

    # Truncate the prompt if it is too long
    for tid in task_ids:
        original_prompt = prompts[tid]
        encoded = trainer.tokenizer(original_prompt, return_tensors="pt", truncation=False)
        length = encoded["input_ids"].shape[1]
        if length > args.max_length:
            print(f"[{tid}] Prompt too long ({length} > {args.max_length}), truncating...")
            truncated_ids = encoded["input_ids"][0][:args.max_length]
            prompts[tid] = trainer.tokenizer.decode(truncated_ids, skip_special_tokens=True)

##############################################################################################
## Start of main loop
    start_time = time.time()
    for start in tqdm(range(0, len(task_ids), args.batch_size),
                  desc="Pipeline Progress",
                  total=(len(task_ids) + args.batch_size - 1) // args.batch_size):  
        end = start + args.batch_size
        id_batch       = task_ids[start:end]
        
        if args.skip_completed:
            id_batch = [tid for tid in id_batch if tid not in completed_ids]
        
        if not id_batch:
            print(f"***No tasks to process in batch {start} to {end}***")
            continue
        
        prompt_batch   = [prompts[tid] for tid in id_batch]
        contract_batch = [contracts_map[tid] for tid in id_batch]
        
        responses = trainer.generate_responses(
            prompt_batch,          
            id_batch,              
            contract_batch,        
            n=args.num_samples,
            skip_map={model_key: completed_ids} if args.skip_completed else None
        )
        
        gen_list = responses.get(model_key, [])

        if gen_list:
            all_generated[model_key].extend(gen_list)
            for rec in gen_list:
                tid = rec.get("task_id")
                if tid is not None:
                    completed_ids.add(tid)

        # if args.use_instruction.startswith("GRAMMAR_ASSERT_SPECIFICATION"):
        #     single_toggle = single_toggles(gen_list[0]['contracts_list'])
        #     all_generated[model_key][start]["single_toggles"] = single_toggle
        
        
        save_json(all_generated, save_root)           
        
    end_time = time.time()
    all_generated['Setting']['time_min'] = (end_time - start_time) / 60

    save_json(all_generated, save_root)
    print(f"[Done] Mode `generate` execution completed. All outputs saved once.")
    
    
        