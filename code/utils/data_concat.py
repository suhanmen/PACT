import json
import pdb
import re
import textwrap
import ast
import math
import inspect
import multiprocessing
import os
from pathlib import Path
from sklearn.model_selection import train_test_split


"""
If you want to concatenate the data, you can use this script.

This script for CODE_GENERATION_CT data.
"""

def data_load(dataset_name, mode):
    with open(f"../../data/code_generation/{dataset_name}/{mode}/o4-mini/total.jsonl", "r") as f:
        data = [json.loads(line) for line in f]
    return data


def save_jsonl(rows, p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        for obj in rows:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    mode = "CODE_GENERATION_CS" # CODE_GENERATION_CS
    
    # for total task ids, we need first CODE_GENERATION_CT total data.
    if mode == "CODE_GENERATION_CS": 
        task_id_list = {}
        with open(f"../../data/code_generation/total/CODE_GENERATION_CT/o4-mini/total.jsonl", "r") as f:
            for line in f:
                item = json.loads(line)
                task_id_list[item['name']] = item
    
    full_data = []
    
    # data_load
    dataset_name = "humaneval"
    humaneval_code_gen_ct_total_data= data_load(dataset_name, mode)
    
    dataset_name = "mbpp"
    mbpp_code_gen_ct_total_data= data_load(dataset_name, mode)
    
    # data_concat
    if mode == "CODE_GENERATION_CS":
        for dataset in [humaneval_code_gen_ct_total_data, mbpp_code_gen_ct_total_data]:
            for item in dataset:
                if item['name'] in task_id_list.keys():
                    full_data.append(item)
                
    else:
        full_data = humaneval_code_gen_ct_total_data + mbpp_code_gen_ct_total_data
    
    # data_save
    out_dir = Path(f"../../data/code_generation/total/{mode}/o4-mini")
    out_dir.mkdir(parents=True, exist_ok=True)
    VALID_RATIO=0.1
    TEST_RATIO=0.1
    SEED=42
    
    train_path = out_dir / "train.jsonl"
    valid_path = out_dir / "valid.jsonl"
    total_path = out_dir / "total.jsonl"
    test_path = out_dir / "test.jsonl"
    
    print(f"[auto] train  → {train_path}")
    print(f"[auto] valid  → {valid_path}")
    print(f"[auto] total  → {total_path}")
    print(f"[auto] test   → {test_path}")
    
    
    # First split: carve out test set
    temp_rows, test_rows = train_test_split(
        full_data,
        test_size=TEST_RATIO,
        random_state=SEED,
        shuffle=True,
    )

    # Second split: split remaining into train/valid
    valid_ratio_within_temp = VALID_RATIO / (1.0 - TEST_RATIO)
    train_rows, valid_rows = train_test_split(
        temp_rows,
        test_size=valid_ratio_within_temp,
        random_state=SEED,
        shuffle=True,
    )

    
    save_jsonl(full_data, total_path)
    save_jsonl(train_rows, train_path)
    save_jsonl(valid_rows, valid_path)
    save_jsonl(test_rows, test_path)