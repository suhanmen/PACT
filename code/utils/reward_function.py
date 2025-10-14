import os, json, sys, io, types
import coverage
from evaluation_model_for_test_case import (
    canonical_solution_load_for_reward,
    safe_eval,
)
from evaluation_contract import collect_assert_ids_from_source,_run_case_trace,_metrics
from inference_parsing import extract_simplified_testcases
from .data_load import load_section
import inspect, tempfile, os
import signal, inspect
import pdb

USE_SECTIONS = set(load_section())        # 5 scenarios for functionality

_error_prefixes = (
    "AssertionError:",
    "Exception:",
    "TypeError:",
    "Timeout",
    "InvalidInput",
)

def _is_error(res):
    return isinstance(res, str) and res.startswith(_error_prefixes)

class TimeoutError(Exception): pass

def _call_with_timeout(func, args, timeout=5):
    """execute in the same process + time limit N seconds"""
    def handler(signum, frame):
        raise TimeoutError("Timeout")
    old_handler = signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)
    try:
        return func(*args)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)

def to_temp_file_and_exec(src_str, entry_point):
    tmp = tempfile.NamedTemporaryFile("w", suffix=".py", delete=False)
    tmp.write(src_str)
    tmp.flush(); tmp.close()

    # exec again to get the function object (fix the file name to tmp.name)
    local_env = {}
    with open(tmp.name, 'r', encoding='utf-8') as f:
        #code_obj = compile(f.read(), tmp.name, "exec")
        code_obj = compile(src_str, tmp.name, 'exec')
        exec(code_obj, local_env)

    return tmp.name, local_env[entry_point]  


# ------------------------------------------------------------------ #
# Functionality Rewarder
# ------------------------------------------------------------------ #
class FunctionalityRewarder:
    def __init__(self, metric_weights=None, corr_weight=0.2, verbose=False):
        self.metric_weights = metric_weights or {'line': 1.0}
        self.corr_weight    = corr_weight
        self._need_branch   = 'branch' in self.metric_weights
        self.verbose        = verbose     # ← whether to print
    # -------------------------------------------------------------- #
    # internal: return detailed metrics after running a single test case ------------------- #
    # -------------------------------------------------------------- #
    def _coverage_reward(self, code_target, test_code):
        cov = coverage.Coverage(branch=self._need_branch, data_file=None)
        cov.start()
        
        # 1) execute
        func_obj, src_str, entry_point = code_target
        target_path, tmp_func = to_temp_file_and_exec(src_str, entry_point)            
        parsed_args = safe_eval(test_code)
        if parsed_args is None:                     # safe_eval failed
            cov.stop()
            return {"line": 0, "branch": 0, "correct": 0, "reward": 0}

        param_count = len(inspect.signature(tmp_func).parameters)
        if param_count == 1:
            if isinstance(parsed_args, (list, tuple)) and len(parsed_args) == 1:
                args_to_pass = [parsed_args[0]]     # remove the shell
            else:
                args_to_pass = [parsed_args]
        else:
            if isinstance(parsed_args, (list, tuple)):
                args_to_pass = parsed_args
            else:
                args_to_pass = [parsed_args]

        try:
            result = _call_with_timeout(tmp_func, args_to_pass, timeout=5)
        except TimeoutError:
            result = "Timeout"
        except AssertionError as e:
            result = f"Exception: {e}"
        except Exception as e:
            result = f"Exception: {e}"
        cov.stop()
        
        
        if any(prefix in str(result) for prefix in _error_prefixes):
            line_ratio = 0
            branch_ratio = 0
            correct = 0
            reward = 0
            return {"line": line_ratio, "branch": branch_ratio,"correct": correct, "reward": reward}
        
        # 2) line·branch coverage (use the original logic)
        _, stmts, _, _, missing_br = cov.analysis2(target_path)
        data = cov.get_data()
        hit_lines = data.lines(target_path) or []
        line_ratio = len(hit_lines) / len(stmts) if stmts else 0.0

        total_b = len(missing_br) + len(data.arcs(target_path) or [])
        hit_b   = len(data.arcs(target_path) or [])
        branch_ratio = hit_b / total_b if total_b else 1.0

        correct = 0 if _is_error(result) else 1
        reward = (self.metric_weights.get('line', 0) * line_ratio +
                self.metric_weights.get('branch', 0) * branch_ratio +
                self.corr_weight * correct)
        
        
        
        return {"line": line_ratio, "branch": branch_ratio,"correct": correct, "reward": reward}
    # -------------------------------------------------------------- #
    # external: return the average reward from multiple test scores ---------------------- #
    # -------------------------------------------------------------- #
    def compute(self, code_target, test_code, return_detail=False):
        detail = self._coverage_reward(code_target, test_code)
        return detail if return_detail else detail["reward"]


# ------------------------------------------------------------------ #
# Contracts Rewarder
# ------------------------------------------------------------------ #

class ContractRewarder:
    def __init__(self,
                 AVC_weight: float = 0.40,
                 TS_weight : float = 0.45,
                 CE_weight : float = 0.15,
                 verbose: bool = False):
        self.W = dict(AVC=AVC_weight, TS=TS_weight, CE=CE_weight)
        self.verbose = verbose

    # ---------- public API -----------------------------------------
    def compute(self,
                reference_src: str,
                entry_point  : str,
                parsed_assert_blocks: dict
               ) -> float:

        #preds = build_assert_predicates(reference_src, entry_point)
        ns: dict[str, Any] = {}
        exec(compile(reference_src, "<contract_src>", "exec"), ns)
        #exec(reference_src, ns)
        fn: types.FunctionType = ns[entry_point]
        param_cnt = len(inspect.signature(fn).parameters)

        #collect assert-line map
        line2id = collect_assert_ids_from_source(reference_src)
        all_ids = set(line2id.values())
        


        fired: Dict[str, Set[str]] = {}
        for aid, cases in parsed_assert_blocks.items():
            print(f"Processing {aid} with {len(cases)} cases")
            for idx, c in enumerate(cases):
                raw = c["input"]
                args_obj = safe_eval(raw) if isinstance(raw, str) else raw

                if param_cnt == 1:
                    if isinstance(args_obj, (list, tuple)) and len(args_obj) == 1:
                        args_to_pass = [args_obj[0]]
                    else:
                        args_to_pass = [args_obj]
                else:
                    args_to_pass = list(args_obj) if isinstance(args_obj,(list,tuple)) else [args_obj]

                ids = _run_case_trace(fn, args_to_pass, line2id)
                fired[f"{aid}#{idx}"] = ids


        reward, detail = _metrics(fired, all_ids, len(fired), self.W)

        if self.verbose:
            print("[Contract metrics]", detail)

        return reward

# ------------------------------------------------------------------ #
# Multi-mode ValidityRewarder
# ---------------------------------rm--------------------------------- #
class ValidityRewarder:
    """
    canon_l   : canonical_solution·entry_point file
    output_jsonl  : model output(jsonl) — here extract contracts(assert list)
    """
    def __init__(self,
                 canon_jsonl,          # ← original DATASET_JSONL
                 output_jsonl,         # ← RAW_OUTPUT_JSONL
                 cov_weights=None, corr_weight=0.2,
                 AVC_weight=0.4, TS_weight=0.45, CE_weight=0.15,
                 a=0.3, 
                 load_variant="no_contracts"):

        # 1) load canonical function
        if 'humaneval' in canon_jsonl.lower():
            self.task_funcs = canonical_solution_load_for_reward('humaneval', load_variant)
        elif 'mbpp' in canon_jsonl.lower():
            self.task_funcs = canonical_solution_load_for_reward('mbpp', load_variant)

        # 2-A) entry_point is read from the canonical file
        self.entry_map = {}
        with open(canon_jsonl, encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                self.entry_map[rec["task_id"]] = rec["entry_point"]

        # 2-B) contracts(assert list) is read from the **model output jsonl**
        self.contracts_map = {}
        with open(output_jsonl, encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                tid = rec["task_id"] if "task_id" in rec else rec["name"]
                # top-level "contract" is used first, if not, use the grammar path
                cdict = rec.get("contract") or rec["grammar"][0]["constraints"][0]
                self.contracts_map[tid] = cdict

        # 3) prepare the rewarder
        self.func_rwd     = FunctionalityRewarder(cov_weights, corr_weight, verbose=True)
        self.contract_rwd = ContractRewarder(AVC_weight, TS_weight, CE_weight, verbose=True)

    # ---------------------------------------------------------- #
    def __call__(self, task_id, raw_output, mode="functionality"):
        contracts = self.contracts_map[task_id]
        entry_fn  = self.entry_map[task_id]          # function name
        try:
            func_obj, src_str, entry_point = self.task_funcs[task_id] # (callable, src)
        except Exception as e:
            print(f"Error loading task {task_id}: {e}")
            pdb.set_trace()

        # ---------- Functionality ----------
        func_reward = 0
        details = []
        if mode in ("functionality", "both"):
            parsed_sec = extract_simplified_testcases(task_id, raw_output,"section", contracts)
            pdb.set_trace()
            scores = []
            for sec, cases in parsed_sec.items():
                if sec not in USE_SECTIONS:
                    continue
                for c in cases:
                    arg_obj = safe_eval(c["input"])              # ← string → object
                    #tc = f"assert {entry_fn}({', '.join(repr(a) for a in arg_obj)})"
                    tc = f"{arg_obj!r}"
                    d = self.func_rwd.compute((func_obj, src_str, entry_point), tc,return_detail=True)
                    
                    w_line    = self.func_rwd.metric_weights.get("line",   0)
                    w_branch  = self.func_rwd.metric_weights.get("branch", 0)
                    w_corr    = self.func_rwd.corr_weight
                    max_score = w_line + w_branch + w_corr        # ← max score
                    
                    raw  = (w_line*d["line"] + w_branch*d["branch"] + w_corr*d["correct"])
                    norm = raw / max_score                        # 0 ≤ norm ≤ 1
                    scores.append(norm)                           # ← normalized score
                    details.append((sec, d))                      # (category, detail)    
            avg_score = sum(scores) / (len(scores) or 1)
            threshold   = 0.8                                # threshold
            func_reward = 1 if avg_score >= threshold else 0
            
            for sec, d in details:
                print(sec, d)
            print(f"avg_score: {avg_score}")
        
        # ---------- Contracts ----------
        contract_reward = 0
        if mode in ("contracts", "both"):
            parsed_assert = extract_simplified_testcases(task_id, raw_output, "assert_specification", contracts)
            
            contract_reward = self.contract_rwd.compute(
                reference_src = src_str,
                entry_point   = entry_point,
                parsed_assert_blocks = parsed_assert
            )
        # ---------- results ----------
        if mode == "functionality":
            return func_reward
        elif mode == "contracts":
            return contract_reward
        else:  # both
            return func_reward + contract_reward

# --------------------------------------------------------------------------- #
# simple execution example
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    data = 'mbpp'
    if data == 'humaneval':
        CANON_JSONL  = "../../data/evalplus-0.1.1/HumanEvalPlus.jsonl"
        #OUTPUT_JSONL = "../gpt_outputs/original/contracts/humaneval_gpt-4o-mini_sft.jsonl"
        OUTPUT_JSONL = "../gpt_outputs/original/functionality/humaneval_gpt-4o-mini_sft.jsonl"
    
    elif data == 'mbpp':
        CANON_JSONL  = "../../data/mbppplus-0.2.0/MbppPlus.jsonl"
        #OUTPUT_JSONL = "../gpt_outputs/original/contracts/mbpp_gpt-4o-mini_sft.jsonl"
        OUTPUT_JSONL = "../gpt_outputs/original/functionality/mbpp_gpt-4o-mini_sft.jsonl"
    # ------------------------------------------------------------------ #
    # A. create a dictionary of {task_id: raw_output(str)} from the model output jsonl
    # ------------------------------------------------------------------ #
    model_out = {}
    with open(OUTPUT_JSONL, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            tid  = rec.get("task_id") or rec["name"]          # either
            raw  = (
                rec.get("output") or                         # depending on the project
                rec.get("raw_output") or
                rec["grammar"][0]["production"][0]           # ← core string
            )
            if raw:
                model_out[tid] = raw
    print(f"✔ model output {len(model_out)} loaded")

    # ------------------------------------------------------------------ #
    # B. initialize the rewarder (contracts are automatically extracted from OUTPUT_JSONL)
    # ------------------------------------------------------------------ #
    if 'functionality' in OUTPUT_JSONL:
        load_variant = "no_contracts"
    else:
        load_variant = "in_contracts"
    
    vr = ValidityRewarder(
        canon_jsonl  = CANON_JSONL,      # canonical solution·entry_point
        output_jsonl = OUTPUT_JSONL,     # contracts location
        cov_weights  = {'line': 0.5, 'branch': 0.5},
        corr_weight  = 0.7,               # coverage only
        load_variant = "in_contracts"
    )
    
    vr.func_rwd.verbose = True 
    # ------------------------------------------------------------------ #
    # C. calculate the reward for one (e.g., HumanEval/23)
    # ------------------------------------------------------------------ #
    for TASK_ID in model_out.keys():
        if TASK_ID not in model_out:
            raise KeyError(f"{TASK_ID} is not in OUTPUT_JSONL.")
        print(f"\n=== {TASK_ID} reward calculation ===")
        print("Functionality :", vr(TASK_ID, model_out[TASK_ID], mode="functionality"))
        #print("Contracts     :", vr(TASK_ID, model_out[TASK_ID], mode="contracts"))
        #print("Total         :", vr(TASK_ID, model_out[TASK_ID], mode="both"))
