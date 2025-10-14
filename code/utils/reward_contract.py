import json, inspect, ast, traceback, types, sys
from typing import Dict, List, Set, Tuple, Any
import json



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

def _run_case_trace(fn, args, line2id):
    """Run the *whole* function; return IDs of asserts that fired (may be ∅)."""
    fired = set()

    def tracer(frame, event, arg):
        if event == "exception":
            exc_type, exc_val, tb = arg
            if exc_type is AssertionError:
                fired_id = line2id.get(frame.f_lineno)
                if fired_id:
                    fired.add(fired_id)
        return tracer

    old = sys.gettrace()
    sys.settrace(tracer)
    try:
        fn(*args)
    except AssertionError:
        pass            # expected for negative tests
    except Exception:
        pass            # treat other errors as miss; fired stays empty
    finally:
        sys.settrace(old)

    return fired





def build_assert_predicates(source: str, entry: str):
    """
    returns dict{ 'a_0': predicate, ... }
    predicate(*args, **kwargs) -> bool  (True == contract holds)
    """
    mod = ast.parse(source)
    fdef = next(n for n in mod.body
                if isinstance(n, ast.FunctionDef) and n.name == entry)
    arg_names = [a.arg for a in fdef.args.args]

    preds = {}
    idx = 0
    print(source)
    for node in fdef.body:
        if isinstance(node, ast.Assert):
            expr = ast.Expression(body=node.test)
            code = compile(expr, filename="<assert_expr>", mode="eval")
            def _make(code_obj):
                return lambda *va, **kw: eval(
                    code_obj, {}, {name: val for name, val in zip(arg_names, va)})
            preds[f"assert_{idx}"] = _make(code)
            print(preds)
            idx += 1
    return preds


def _metrics(fired: Dict[str, Set[str]], all_ids: Set[str],
             total_tests: int, w: Dict[str, float]) -> Tuple[float, Dict[str, float]]:
    covered = {aid for s in fired.values() for aid in s if aid in all_ids}
    avc = len(covered)/len(all_ids) if all_ids else 0.0
    extras = sum(max(len(v)-1, 0) for v in fired.values())
    totalF = sum(len(v) for v in fired.values())
    ts = 1.0 - extras/totalF if totalF else 0.0
    ce = avc/total_tests if total_tests else 0.0
    tqs = w["AVC"]*avc + w["TS"]*ts + w["CE"]*ce
    return tqs, dict(AVC=avc, TS=ts, CE=ce, TQS=tqs)


def compute_score(
    contract_testcases: str,          # negative tests JSON
    reference_src: str,         # <— the reference code as text
    entry_name: str,            # name of the function inside that code
    AVC_weight: float,
    TS_weight: float,
    CE_weight: float
) -> float:
    try:
        # 1) build the reference function object from the source
        ns: dict[str, any] = {}
        exec(reference_src, ns)  # execute the source code

        ref_fn: types.FunctionType = ns[entry_name]

        # 2) collect assert-ids directly from the same source string
        line2id = collect_assert_ids_from_source(reference_src)
        all_ids = set(line2id.values())

        # 3) load test suites
        neg_suite = json.loads(contract_testcases)

        # 4) run tests  (use same _run_case, _metrics helpers as before)
        fired = {}
        for g, tests in neg_suite.items():
            for i, case in enumerate(tests):
                ok, ids = _run_case(ref_fn, case["input"], line2id)
                fired[f"{g}#{i}"] = ids

        Weights = dict(AVC=AVC_weight, TS=TS_weight, CE=CE_weight)


        reward, detail = _metrics(fired, all_ids, len(fired), Weights)
        return reward, detail

    except Exception:
        traceback.print_exc()           # optional: show why it failed
        return 0.0, None





if __name__ == "__main__":
    reference_code = """
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    assert isinstance(threshold, float) and threshold > 0        # a_0
    assert isinstance(numbers, list)                             # a_1
    assert all(isinstance(v, (int, float)) for v in numbers)     # a_2
    numbers = sorted(numbers)
    return any(b - a < threshold for a, b in zip(numbers, numbers[1:]))
    """

    negative_tests = { "assert_0": [{"input": [[1.0], "bad"]}, {"input": [[1.0], -0.1]}], "assert_1": [{"input": ["oops", 0.4]} ], "assert_2": [  {"input": [["str", 2.0], 0.3]}   ] }

    r,detail = compute_score(
            contract_testcases=json.dumps(negative_tests),
            reference_src=reference_code,
            entry_name="has_close_elements",
            AVC_weight=0.40,
            TS_weight=0.45,
            CE_weight=0.15
    )

    print("reward =", r)
    print("detail =", detail)
