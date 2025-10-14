import os
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Union
import pdb
import openai
from tqdm import tqdm
import ast 
import re
import textwrap
from utils.Instruction import instruction_template
from utils.data_load import load_data
from json import JSONDecoder
import random, time
from openai.error import (
    ServiceUnavailableError, RateLimitError, APIError, Timeout, OpenAIError
)

def load_done_ids(jsonl_path: Path) -> set[str]:
    """Return the set of task_ids already written to *raw* output."""
    if not jsonl_path.exists():
        return set()
    done = set()
    with open(jsonl_path, encoding="utf-8") as f:
        for line in f:
            try:
                done.add(json.loads(line)["task_id"])
            except Exception:
                # damaged line → skip, but keep going
                continue
    return done

def chat_completion_retry(*, model, messages, temperature, n,
                          max_retries: int = 6,
                          backoff_base: float = 2,
                          backoff_cap: float = 60):
    """Wrapper that retries on transient OpenAI errors with exp. back‑off."""
    for attempt in range(max_retries):
        try:
            return openai.ChatCompletion.create(
                model=model, messages=messages,
                temperature=temperature, n=n
            )
        except (ServiceUnavailableError, RateLimitError,
                Timeout, APIError, OpenAIError) as e:
            if attempt == max_retries - 1:
                raise
            sleep = min(backoff_base ** attempt + random.random(), backoff_cap)
            print(f"[retry {attempt+1}/{max_retries}] {type(e).__name__}: {e}. "
                  f"Sleeping {sleep:.1f}s")
            time.sleep(sleep)


def load_jsonl_to_dict(jsonl_path: str) -> Dict[str, Dict]:
    """Convert EvalPlus‑style *.jsonl to a task‑id‑keyed dict."""
    task_map: Dict[str, Dict] = {}
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            task_id = obj["task_id"]
            task_map[task_id] = {
                "prompt": obj["prompt"],
                "contract": obj["contract"],
                "canonical_solution": obj["canonical_solution"],
                "entry_point": obj.get("entry_point", "solution"),
            }
    return task_map

def _build_contract_str(contracts: Union[str, List, Dict]) -> str:
    """Flatten / normalise contract snippets into labelled `assert_N: ...` lines."""
    if not contracts:
        return ""

    # 0) flatten nested list
    if isinstance(contracts, list):
        flat: List[str] = []
        for item in contracts:
            flat.extend(item.values() if isinstance(item, dict) else [str(item)])
        contracts = "\n".join(flat)

    # 1) dict → list of values ordered by numeric index in key if present
    if isinstance(contracts, dict):
        def k_order(k):
            m = re.search(r"\d+", k)
            return int(m.group()) if m else k
        lines = [contracts[k] for k in sorted(contracts, key=k_order)]
    else:
        # try json first
        try:
            obj = json.loads(contracts)
            if isinstance(obj, dict):
                lines = [obj[k] for k in sorted(obj)]
            else:
                lines = str(contracts).splitlines()
        except json.JSONDecodeError:
            lines = str(contracts).splitlines()

    cleaned: List[str] = []
    for raw in lines:
        raw = str(raw).strip().replace("# $_CONTRACT_$", "").strip(" ,\"")
        if raw.startswith("assert "):
            cleaned.append(raw)
    return "\n".join(f"assert_{i}: {c}" for i, c in enumerate(cleaned)) + ("\n" if cleaned else "")

def _inject_contracts_into_solution(sol, contracts, entry):
    if not contracts.strip():
        return sol
    # search for entry-point header
    pat = rf'^\s*def\s+{re.escape(entry)}\s*\([^)]*\)[^\n]*:'
    m = re.search(pat, sol, flags=re.MULTILINE)
    if not m:
        return sol
    header_end = m.end()
    indent = " " * 0                       # ← 4 spaces
    indented = textwrap.indent(contracts.rstrip("\n"), indent)
    return sol[:header_end] + "\n" + indented + "\n" + sol[header_end:].lstrip("\n")

def make_messages(dataset,
                  example,
                  use_instruction,
                  dataset_type):
    """Return list[{"role", "content"}] ready for ChatCompletion."""
    instruction, output_instruction = instruction_template(use_instruction)
    entry    = example.get("entry_point", "")
    desc     = example.get("prompt", "")
    sol      = example.get("canonical_solution", "")
    tests    = example.get("test", [])  # may be missing
    contracts = example.get("contract", "")
    contracts_str = _build_contract_str(contracts)

    # minimal set replicating logic in main.py
    if use_instruction in ["HUMANEVAL_MASK_STRING", "MBPP_MASK_STRING"]:
        user_content = (
                    f"Method Name: {entry}\n"
                    f"Problem Description:\n{desc}\n\n"
                    f"Contract List:\n{contracts_str}\n"
                    f"{output_instruction}"
            )
    
    elif use_instruction == "INDIVIDUAL_MASK_STRING":
        if dataset_type == 'humaneval':
            user_content = (
                    f"Method Name: {entry}\n"
                    f"Code:\n{desc}{sol}\n"
                    f"Contract List:\n{contracts_str}\n"
                    f"{output_instruction}"
            )
        elif dataset_type == 'mbpp':
            user_content = (
                    f"Method Name: {entry}\n"
                    f"Code:\n{sol}\n"
                    f"Contract List:\n{contracts_str}\n"
                    f"{output_instruction}"
            )
        
    elif use_instruction in ['ASSERT_SPECIFICATION', 'FUNCTIONALITY_SPECIFICATION', 'MULTI_ASSERT_SPECIFICATION']:    
        if dataset_type == 'humaneval':
            user_content = (
                        f"Method Name: {entry}\n"
                        f"Problem Description:\n{desc}\n"
                        f"{contracts}"
                        f"{sol}\n\n"
                        f"Contract List:\n{contracts_str}\n"
                        f"{output_instruction}"
                )
        elif dataset_type == 'mbpp':
            sol_with_contracts = _inject_contracts_into_solution(sol, contracts, entry)
            user_content = (
                    f"Method Name: {entry}\n"
                    f"Problem Description:\n{desc}\n"
                    f"{sol_with_contracts}\n\n"
                    f"Contract List:\n{contracts_str}\n"
                    f"{output_instruction}"
            )
    elif use_instruction == "GRAMMAR_ASSERT_SPECIFICATION":
        if dataset_type == 'humaneval':
            user_content = (
                f"{output_instruction}\n"
                f"Method Name: {entry}\n"
                f"Problem Description:\n{desc}\n"
                f"{contracts}"
                f"{sol}\n\n"
                f"Contract List:\n{contracts_str}\n"     
                )
        elif dataset_type == 'mbpp':
            sol_with_contracts = _inject_contracts_into_solution(sol, contracts, entry)
            user_content = (
                f"{output_instruction}\n"
                f"Method Name: {entry}\n"
                f"Problem Description:\n{desc}\n"
                f"{sol_with_contracts}\n\n"
                f"Contract List:\n{contracts_str}\n"
            )
    
    elif use_instruction == "CODE_GENERATION_CT":
        return [
            {"role": "system", "content": example["description"][0]["content"]},
            {"role": "user", "content": example["description"][1]["content"]},
        ]
     
    return [
        {"role": "system", "content": instruction},
        {"role": "user", "content": user_content},
    ]

def load_dataset(dataset: str):
    """Return dict keyed by task_id with example objects."""
    if dataset == "humaneval":
        return load_jsonl_to_dict("../../data/evalplus-0.1.1/HumanEvalPlus.jsonl")
    if dataset == "mbpp":
        return load_jsonl_to_dict("../../data/mbppplus-0.2.0/MbppPlus.jsonl")
    # else: rely on utility loader (could be HuggingFace Dataset or our custom format)
    ds = load_data(dataset)
    # utils.load_data() may return DatasetDict; pick test split if present
    return ds["test"] if hasattr(ds, "keys") and "test" in ds.keys() else ds

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset", required=True, help="Dataset name (e.g. humaneval)")
    p.add_argument("--use_instruction", default="None", help="Which instruction template to load via utils.Instruction.instruction_template")
    p.add_argument("--model", default="gpt-4o-mini", help="OpenAI ChatCompletion model")
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--num_samples", type=int, default=1, help="Responses per prompt")
    p.add_argument("--output_dir", default="./outputs", help="Where to write JSONL results")
    p.add_argument("--open_api_key")
    return p.parse_args()


def extract_json_after_think(txt: str) -> str | None:
    parts = re.split(r"</think>", txt, flags=re.I | re.S)
    if len(parts) < 2:
        return None
    tail = parts[1].lstrip()

    if not tail.startswith("{"):
        brace_pos = tail.find("{")
        if brace_pos == -1:
            return None
        tail = tail[brace_pos:]

    decoder = JSONDecoder()
    try:
        _, end = decoder.raw_decode(tail)
        return tail[:end].strip()     
    except json.JSONDecodeError:
        return None


def sft_format_json(task_id, messages, response_content, constraints):
    """Convert a single assistant response into SFT‑ready JSON.

    Schema
    ------
    {
      "name": taskid,
      "description": messages,  # raw prompt/assistant messages list
      "grammar": [
        {
          "production": <JSON code block with assert testcases>,
          "constraints": <string of constraints>
        }
      ],
      "reasoning": <content inside <think> ... </think>>
    }
    """
    # 1) reasoning (text between <think> ... </think>)
    think_match = re.search(r"<think>(.*?)</think>", response_content, re.DOTALL | re.IGNORECASE)
    reasoning = think_match.group(1).strip() if think_match else ""

    # 2) production → JSON code block content (keep raw to avoid parsing issues with comments)
    prod_match = re.search(r"```json\s*(.*?)\s*```", response_content, re.DOTALL | re.IGNORECASE)
    if prod_match:
        production_raw = prod_match.group(1).strip()
    else:
        production_raw = extract_json_after_think(response_content)
        print(f"********* Use extract_json_after_think **********")
        if production_raw is None:
            print(f"********* [{task_id}] JSON block not found. **********")
            return None

    contract_dict = {}
    for line in constraints.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            contract_dict[key.strip()] = val.strip()
    
    return {
        "name": task_id,
        "description": messages,
        "grammar": [{
            "production": [production_raw],
            "constraints": [contract_dict]
        }],
        "reasoning": [reasoning + '</think>'],
    }

def sft_format_json_mask(task_id, messages, response_content, constraints):
    prod_match = re.search(r"```python\s*(.*?)\s*```", response_content, re.DOTALL | re.IGNORECASE)
    production_raw = prod_match.group(1).strip()

    contract_dict = {}
    for line in constraints.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            contract_dict[key.strip()] = val.strip()
    return {
        "name": task_id,
        "description": messages,
        "grammar": [{
            "production": [production_raw],
            "constraints": [contract_dict]
        }]
    }

def sft_format_json_individual(task_id, messages, response_content, constraints):
    prod_match = re.search(r"```json\s*(.*?)\s*```", response_content, re.DOTALL | re.IGNORECASE)
    production_raw = prod_match.group(1).strip()

    contract_dict = {}
    for line in constraints.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            contract_dict[key.strip()] = val.strip()

    return {
        "name": task_id,
        "description": messages,
        "grammar": [{
            "production": [production_raw, json.loads(production_raw)],
            "constraints": [contract_dict]
        }]
    }

def main():
    args = parse_args()
    openai.api_key = args.open_api_key
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable missing")
    dataset = load_dataset(args.dataset)
    task_ids = list(dataset.keys())

    #task_ids = ['HumanEval/21']
    
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    
    if args.use_instruction == "CODE_GENERATION_CT":
        load_dataset_ct_path = f"../../data/code_generation/{args.dataset}/CODE_GENERATION_CT/o4-mini/total.jsonl"
        with open(load_dataset_ct_path, "r", encoding="utf-8") as f:
            dataset = {}
            task_ids=[]
            for line in f:
                obj = json.loads(line)
                dataset[obj["name"]] = obj
                task_ids.append(obj["name"])            
        
    raw_outfile  = Path(args.output_dir) / f"{args.dataset}_{args.model}_raw.jsonl"
    sft_outfile  = Path(args.output_dir) / f"{args.dataset}_{args.model}_sft.jsonl"

    done_ids = load_done_ids(raw_outfile)          # ❶ resume support
    max_regen = 3                                  # ❷ JSON‑parse retry ceiling

    with open(raw_outfile, "a", encoding="utf-8") as raw_f, \
         open(sft_outfile, "a", encoding="utf-8") as sft_f:  # append‑mode!
        for tid in tqdm(task_ids, desc="Querying OpenAI", unit="task"):
            if tid in done_ids:
                continue                           # already processed
            
            # # Debugging #########################################################
            # if tid != "HumanEval/76":
            #     continue
            # #####################################################################
            
            example   = dataset[tid]
            messages  = make_messages(args.dataset, example,
                                       args.use_instruction, args.dataset)
            
            regen_attempt = 0
            while True:                            # ❸ regenerate loop
                try:
                    result = chat_completion_retry(
                        model=args.model,
                        messages=messages,
                        temperature=args.temperature,
                        n=args.num_samples
                    )
                except OpenAIError as e:
                    print(f"[{tid}] fatal OpenAI error → skip: {e}")
                    break

                result_dict      = result.to_dict_recursive()
                print(tid)
                print(messages[0]['content'])
                print(messages[1]['content'])
                print(result.to_dict_recursive()['choices'][0]['message']['content'])
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------\n\n')
                # -- write raw record ------------------------------------------------
                
                response_content = result_dict["choices"][0]["message"]["content"]
                
                #pdb.set_trace()
               
                # --- write raw immediately (so we never lose anything) -------
                raw_record = {
                    "task_id": tid,
                    "messages": messages,
                    "response": result_dict
                }
                raw_f.write(json.dumps(raw_record, ensure_ascii=False) + "\n")
                raw_f.flush()

                # --- build SFT record ----------------------------------------
                contract_str = _build_contract_str(example.get("contract"))
                try:
                    if args.use_instruction in {"HUMANEVAL_MASK_STRING",
                                                "MBPP_MASK_STRING"}:
                        sft_record = sft_format_json_mask(
                            tid, messages, response_content, contract_str)
                    elif args.use_instruction == "INDIVIDUAL_MASK_STRING":
                        sft_record = sft_format_json_individual(
                            tid, messages, response_content, contract_str)
                    else:
                        sft_record = sft_format_json(
                            tid, messages, response_content, contract_str)
                except Exception as e:
                    sft_record = None              # parsing blew up

                # --- success path -------------------------------------------
                if sft_record is not None:
                    sft_f.write(json.dumps(sft_record, ensure_ascii=False) + "\n")
                    sft_f.flush()
                    break                          # done with this task

                # --- JSON invalid → regenerate or give up -------------------
                regen_attempt += 1
                if regen_attempt >= max_regen:
                    print(f"[{tid}] Could not produce valid JSON after "
                          f"{max_regen} tries → skipping.")
                    break
                print(f"[{tid}] Invalid JSON, regenerating ({regen_attempt}/{max_regen})…")

if __name__ == "__main__":
    main()
