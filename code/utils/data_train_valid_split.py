import argparse, json, csv
from pathlib import Path
from sklearn.model_selection import train_test_split
import pdb

def load_jsonl(p: Path):
    return [json.loads(l) for l in p.open(encoding="utf-8")]

def save_jsonl(rows, p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        for obj in rows:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")

def test_load_jsonl(test_case_type, model, dataset):
    if dataset == "mbpp":
        test_data_tpye = "humaneval"
    elif dataset == "humaneval":
        test_data_tpye = "mbpp"
    
    if test_case_type == "grammar_assert_specification":
        data_path = f"../../code/output_gpt/{test_data_tpye}/after_quality/{test_case_type}/{model}/{model}_train_data.jsonl"
    else:
        data_path = f"../../code/output_gpt/original/{model}/{test_case_type}/{test_data_tpye}_{model}_sft.jsonl"
    
    return [json.loads(l) for l in Path(data_path).open(encoding="utf-8")]

def main():
    ap = argparse.ArgumentParser(description="Split JSONL into train/valid sets and save summary CSV")
    ap.add_argument("--data", required=True, help="original JSONL path")
    ap.add_argument("--valid-ratio", type=float, default=0.1, help="validation ratio (default 0.1)")
    ap.add_argument("--seed", type=int, default=42, help="Random seed (default 42)")
    ap.add_argument("--model", required=True, help="model name")
    ap.add_argument("--test_case_type", required=True, help="test case type")
    ap.add_argument("--dataset", required=True, help="dataset name")
    args = ap.parse_args()

    data_path = Path(args.data).resolve()
    if "grammar_assert_specification" == args.test_case_type:
        dataset_dir = data_path.parent.parent.parent.parent
    else:
        dataset_dir = data_path.parent.parent.parent  # .../<dataset>/after_quality/<basename>.jsonl
    out_dir = dataset_dir / "train_valid" / args.test_case_type / args.model
    out_dir.mkdir(parents=True, exist_ok=True)

    # Paths
    train_path = out_dir / "train.jsonl"
    valid_path = out_dir / "valid.jsonl"
    total_path = out_dir / "total.jsonl"
    test_path = out_dir / "test.jsonl"
    summary_csv = out_dir / "split_summary.csv"

    print(f"[auto] train  → {train_path}")
    print(f"[auto] valid  → {valid_path}")
    print(f"[auto] total  → {total_path}")
    print(f"[auto] test   → {test_path}")

    # Load and split
    rows = load_jsonl(data_path)
    train_rows, valid_rows = train_test_split(
        rows,
        test_size=args.valid_ratio,
        random_state=args.seed,
        shuffle=True,
    )

    # Load test cases
    test_rows = test_load_jsonl(args.test_case_type, args.model, args.dataset)
    
    # Save splits
    save_jsonl(train_rows, train_path)
    save_jsonl(valid_rows, valid_path)
    save_jsonl(rows, total_path)
    save_jsonl(test_rows, test_path)

    # Summary info
    train_count = len(train_rows)
    valid_count = len(valid_rows)
    test_count = len(test_rows)
    total_count = len(rows)
    # Write summary CSV
    with summary_csv.open('w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['data_file', 'valid_ratio', 'seed', 'train_count', 'valid_count', 'train_path', 'valid_path'])
        writer.writerow([
            str(data_path).split('/')[-1], args.valid_ratio, args.seed,
            train_count, valid_count,
            str(train_path), str(valid_path)
        ])

    print(f"✔ Train: {train_count:>5} → {train_path}")
    print(f"✔ Valid: {valid_count:>5} → {valid_path}")
    print(f"✔ Total: {total_count:>5} → {total_path}")
    print(f"✔ Test: {test_count:>5} → {test_path}")
    print(f"Saved split summary CSV to: {summary_csv}")

if __name__ == "__main__":
    main()
