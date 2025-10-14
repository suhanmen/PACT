import json, os
from textwrap import indent
from collections import defaultdict
from collections import OrderedDict 
import pdb
import re

########################################################################################################################
# mask string instruction
# For gpt-4o-mini instructions to make contracts natural language
HUMANEVAL_MASK_STRING = """
You are an expert program analyst.

I will provide:
- Method Name: the name of the function to test.
- Problem Description: a natural language description of what the function is supposed to do, including its expected behavior, input constraints (as assertions), and a reference implementation.
- Contract List: a list of input validation conditions written as assertions that enforce type, range, and structural constraints before executing the main logic.

Your task is:
1. **Rewrite the summary line**  
  - Find the **first sentence** of the function’s docstring.  
  - Rewrite it so it still describes the purpose **and** *spells out* every constraint from **Contract List** in plain prose (no parentheses, no bullet lists).  
    *Example style →*  
    Check whether any two numbers in the given list are closer than the threshold; “numbers” must be a list of ints or floats, and “threshold” must be a positive float.  
  - Leave everything else (code, examples, rest of docstring) unchanged.

2. **Output**  
  - Return **one Markdown string** containing a python code block with the fully rewritten source.  
  - Do **not** add commentary outside the code block.
"""

MBPP_MASK_STRING = """
You are an expert program analyst.

I will provide:
- Method Name: the name of the function to test.
- Problem Description: a one-sentence description of what the function is supposed to do, followed by one or more example assertions.
- Contract List: a list of input-validation assertions that enforce type, range, and structural constraints before executing the main logic.

Your task is:
1. **Rewrite only the first sentence of the Problem Description block**  
    - Replace that sentence with a new one that **begins with**  
      `Write a python function that …`  
      and then (a) explains the function’s purpose and (b) *spells out* every constraint in **Contract List** in plain prose (no parentheses, no bullet lists).  
      *Example style →*  
      `Write a python function that returns the shared elements from two tuples; “test_tup1” and “test_tup2” must each be tuples.`

2. **Preserve everything else**  
    - After your new first sentence, leave **one blank line** and copy the remainder of the original Problem Description block **unchanged** (including all example `assert` lines).  
    - Do **not** add or modify any other code.

3. **Output**  
    - Return **one Markdown string** whose entire content is a ```python``` fenced code block containing **only the rewritten triple-quoted Problem Description string**.
"""

OUTPUT_INSTRUCTION_MASK_STRING = """
----------------------------------------
Produce the final Markdown string now.

### Implementation Guidelines
```python

...

```
----------------------------------------
"""

INDIVIDUAL_MASK_STRING = """
You are an expert program analyst.

I will provide:
- Method Name: the name of the function to test.
- Code: the canonical solution code.
- Contract List: a list of input-validation assertions that enforce type, range, and structural constraints before executing the main logic.

Your task is:
- For each item in the Contract List, write a clear and precise natural language sentence that explains the constraint.  
  Each explanation must be a standalone sentence, written without parentheses or code formatting.  
  Be concise but unambiguous.

- Do not include any other information such as the function’s purpose, method name, or example assertions.

- Return your output as a JSON object.  
  Each key should be in the format "assert_0", "assert_1", ..., and the value should be the corresponding natural language explanation as a string.
"""

OUTPUT_INSTRUCTION_INDIVIDUAL_MASK_STRING = """
----------------------------------------
Respond in structured JSON format.

You must begin your response with ```json and end it with ```.
### Implementation Guidelines
```json
{
  "assert_0": '...',
  "assert_1": '...',
  ...
}
```
----------------------------------------
"""
########################################################################################################################
# Not Use functionality test case instruction

INSTRUCTION_10 = """
You are an expert program analyst.

I will provide:
- Method Name: a function or method name that defines the main entry point.
- prompt: natural language description of the task to solve.
- canonical_solution: reference code
- test_cases: existing tests

The current test_cases may not fully cover important corner cases or execution paths.
Your task is to generate additional, high-quality test cases for the following categories:

1. Boundary Cases — test inputs at the edge of valid ranges (e.g., empty inputs, max length, min values).
2. Edge Cases — uncommon but valid inputs that may trigger corner behavior.
3. Invalid Inputs — inputs that violate the expected constraints or types (for robustness testing).
4. Performance Constraints — inputs that stress time or space limits (e.g., large arrays, deep recursion).
5. Exception Scenarios — inputs that are expected to raise exceptions or trigger fallback logic.
6. Line Coverage Targets — inputs designed to execute previously uncovered lines of code.
7. Branch Coverage Targets — inputs that force each conditional branch to be taken.
8. Condition Coverage Targets — inputs that explore all possible boolean subconditions within complex expressions.
9. Function Coverage — ensure that all helper functions in the code are invoked.
10. Path Coverage (Advanced) — inputs that exercise distinct execution paths through the function.

Ensure that:
- Each category contains at least one distinct test cases.
- Test cases do not overlap between categories.
- You do not duplicate the existing test cases provided.
- All responses must strictly adhere to the JSON format shown below.

Each test case must include the following fields:
- input: the argument(s) to pass to the function
- expected_output: the return value expected from the function
- explanation: a concise 1–2 sentence justification of why this test case is important and what code behavior or logic it targets
  """

OUTPUT_INSTRUCTION_10 = """
----------------------------------------
Respond in structured JSON format, grouped by each category. For each test case, provide:

{
  "boundary_cases": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "edge_cases": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "invalid_inputs": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "performance_constraints": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "exception_scenarios": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "line_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <specify the specific line(s) of code this input is designed to execute>
    }
  ],
  "branch_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <specify which branch (e.g., if/else, switch-case) this test aims to cover>
    }
  ],
  "condition_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <specify which boolean subcondition(s) are being exercised>
    }
  ],
  "function_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <mention the helper function or specific method this input is intended to invoke>
    }
  ],
  "path_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <describe the specific control flow path this test is designed to traverse>
    }
  ]
}
----------------------------------------
  """

OUTPUT_EX_INSTRUCTION_10 = """
----------------------------------------
Respond in structured JSON format, grouped by each category. For each test case, provide:

{
  "boundary_cases": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "edge_cases": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "invalid_inputs": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "performance_constraints": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "exception_scenarios": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <briefly explain why this case is important and what part of the code it is intended to cover>
    }
  ],
  "line_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <specify the specific line(s) of code this input is designed to execute>
    }
  ],
  "branch_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <specify which branch (e.g., if/else, switch-case) this test aims to cover>
    }
  ],
  "condition_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <specify which boolean subcondition(s) are being exercised>
    }
  ],
  "function_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <mention the helper function or specific method this input is intended to invoke>
    }
  ],
  "path_coverage_targets": [
    {
      "input": <args>,
      "expected_output": <return>,
      "explanation": <describe the specific control flow path this test is designed to traverse>
    }
  ]
}

Example:
{
  "boundary_cases": [
    {
      "input": [[], 0.5],
      "expected_output": false,
      "explanation": "Empty list with threshold 0.5 should return false, covering the base-case early return."
    }
  ],
  "edge_cases": [
    {
      "input": [[1, 2, -3], 1],
      "expected_output": true,
      "explanation": "List containing a negative value tests absolute-difference logic in a non-trivial scenario."
    }
  ],
  "invalid_inputs": [
    {
      "input": ["not a list", 1],
      "expected_output": null,
      "explanation": "Non-list first argument should raise a TypeError to validate input type checking."
    }
  ],
  "performance_constraints": [
    {
      "input": [list(range(100000)), 0],
      "expected_output": false,
      "explanation": "Very large list with threshold 0 stresses time complexity, ensuring performance requirements."
    }
  ],
  "exception_scenarios": [
    {
      "input": [[1, 2, 3], -1],
      "expected_output": null,
      "explanation": "Negative threshold should trigger a ValueError in argument validation logic."
    }
  ],
  "line_coverage_targets": [
    {
      "input": [[1, 1], 1],
      "expected_output": true,
      "explanation": "Executes the line that detects identical elements at index pair (0,1)."
    }
  ],
  "branch_coverage_targets": [
    {
      "input": [[1, 3, 5], 1],
      "expected_output": false,
      "explanation": "Covers the else branch where no two elements are within threshold."
    }
  ],
  "condition_coverage_targets": [
    {
      "input": [[1, 2, 4], 3],
      "expected_output": false,
      "explanation": "Exercises both subconditions in the combined boolean (abs(a - b) < threshold) check."
    }
  ],
  "function_coverage_targets": [
    {
      "input": [[2, 5, 7], 3],
      "expected_output": true,
      "explanation": "Invokes the helper function compute_diff to calculate absolute differences."
    }
  ],
  "path_coverage_targets": [
    {
      "input": [[0, 2, 4, 6], 2],
      "expected_output": true,
      "explanation": "Traverses nested loops fully until early return on first qualifying pair."
    }
  ]
}
----------------------------------------
  """
########################################################################################################################
# assertion specification

ASSERT_SPECIFICATION = """
You are an expert program analyst.

I will provide:
{header_fields}

Your task is:
- For **each assertion (contract) in the Contract List**, generate **5 distinct test cases** that intentionally violate **that specific contract**.
- **Before emitting any JSON, write a very short chain-of-thought wrapped in `<think>…</think>` (3–4 sentences) explaining your overall violation strategy.**
- Ensure each test case remains functionally meaningful, but is intentionally designed to violate the assertion logic (e.g., incorrect types, invalid ranges, malformed structure).
- Do not generate duplicate or overlapping test cases across assertions.
- Assume the goal is to test how well the function enforces input validation via assertions.

JSON Rules (STRICT)
- **Absolutely NO comments** (`// …` or `# …`) and no trailing commas.
- Use JSON literals only: `null` (not `None`), `true/false` (not `True/False`).
- Do not output tuples; use lists `[...]` only.
- input: the **list of arguments** to pass to the function that would trigger the assertion failure.
- Each test case must strictly follow the ```json ...``` format as shown below.
"""

OUTPUT_INSTRUCTION_ASSERTIONS = """
----------------------------------------
**Before emitting the JSON object, write a very short `<think>…</think>` block (3–4 sentences) with your overall strategy.**
Respond in structured JSON format, grouped by each assertion being violated.
For each violated assertion, provide exactly **5** distinct test cases.
Each test case must be a dictionary containing:
- "input": list of arguments that would trigger the assertion error.

### Implementation Guidelines
<think>
...
</think>

```json
{
  "assert_0": [
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] }
  ],
  "assert_1": [
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] }
  ],
  ...
```
----------------------------------------
  """

MULTI_ASSERT_SPECIFICATION = """
You are an expert program analyst.

I will provide:
{header_fields}

Your task is:
1) **CRITICAL**: Ensure ALL inputs satisfy basic structural requirements so the program can execute (e.g., correct types, minimum lengths, basic structure).
2) **For each assertion (contract) in the Contract List**, generate **5 distinct test cases** that intentionally violate **that specific contract** while keeping ALL OTHER contracts satisfiable.
3) You MUST generate all possible contract-violation groups.
   - Let **N = the number of assertions in the Contract List**.
   - You MUST output exactly **(2^N - 1)** groups (every non-empty subset of assertions).
   - **Do not skip or omit any group.** Partial coverage is strictly forbidden.
   - **Each group MUST contain exactly 5 test cases.** No more, no less.
   - **Group key naming**: use comma-separated assertion IDs in ascending order, e.g., "assert_0", ... "assert_0,assert_1", ... "assert_0,assert_1,assert_2".
   - **Ordering**: sort groups by the number of violated assertions (ascending), then lexicographically by the group key.
4) **Before emitting any JSON, write a very short chain-of-thought wrapped in `<think>…</think>` (3–4 sentences) explaining your overall violation strategy.**
5) Ensure each test case remains functionally meaningful, but is intentionally designed to violate the assertion logic (e.g., incorrect types, invalid ranges, malformed structure).
6) Do not generate duplicate or overlapping test cases across assertions.
7) Assume the goal is to test how well the function enforces input validation via assertions.

JSON Rules (STRICT)
- **Absolutely NO comments** (`// …` or `# …`) and no trailing commas.
- Use JSON literals only: `null` (not `None`), `true/false` (not `True/False`).
- Do not output tuples; use lists `[...]` only.
- input: the **list of arguments** to pass to the function that would trigger the assertion failure.
- Each test case must strictly follow the ```json ...``` format as shown below.
"""

MULTI_OUTPUT_INSTRUCTION_ASSERTIONS = """
----------------------------------------
**Before emitting the JSON object, write a very short `<think>…</think>` block (3–4 sentences) with your overall strategy.**
Respond in structured JSON format, grouped by each assertion being violated.
For each violated assertion, provide exactly **5** distinct test cases.
Each test case must be a dictionary containing:
- "input": list of arguments that would trigger the assertion error.

### Implementation Guidelines
<think>
...
</think>

```json
{
  "assert_0": [
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] }
  ],
  "assert_1": [
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] }
  ],
  "assert_2": [
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] }
  ],
  "assert_0,assert_1": [
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] }
  ],
  "assert_0,assert_2": [
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] },
    { "input": [...] }
  ],
  ... 
}
```
----------------------------------------
"""

ASSERT_SPECIFICATION = ASSERT_SPECIFICATION.format(
  header_fields="""
- Method Name: the name of the function to test.
- Problem Description: a natural language description of what the function is supposed to do, including its expected behavior, input constraints (as assertions), and a reference implementation.
- Contract List: a list of input validation conditions written as assertions that enforce type, range, and structural constraints before executing the main logic.
  """
)

MULTI_ASSERT_SPECIFICATION = MULTI_ASSERT_SPECIFICATION.format(
  header_fields="""
- Method Name: the name of the function to test.
- Problem Description: a natural language description of what the function is supposed to do, including its expected behavior, input constraints (as assertions), and a reference implementation.
- Contract List: a list of input validation conditions written as assertions that enforce type, range, and structural constraints before executing the main logic.
  """
)

HUMANEVAL_DIRECT_EXAMPLE = '''
Method: safe_divide
Problem Description:
def safe_divide(a, b):
    """Return a / b if b != 0 else None.
    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(5, 0)
    None
    """

    assert isinstance(a, (int, float)), "invalid inputs"  # $_CONTRACT_$
    assert isinstance(b, (int, float)), "invalid inputs"  # $_CONTRACT_$
    assert b != 0, "invalid inputs"  # $_CONTRACT_$

    return a / b

Contract List:
assert_0: assert isinstance(a, (int, float)), "invalid inputs"
assert_1: assert isinstance(b, (int, float)), "invalid inputs"
assert_2: assert b != 0, "invalid inputs"

<think>
I will declare inputs `a` and `b` as Value types, then encode each Python assert as a Bool predicate C0–C2. Basic structure constraints ensure executability while contract predicates model the assertion semantics.
</think>
{
  "assert_0": [
    { "input": ["not_a_number", 5.0] },
    { "input": [None, 2.0] },
    { "input": [True, 3.0] },
    { "input": [{"key": "value"}, 1.0] },
    { "input": [[1, 2, 3], 4.0] }
  ],
  "assert_1": [
    { "input": [10.0, "not_a_number"] },
    { "input": [5.0, None] },
    { "input": [2.0, False] },
    { "input": [1.0, {"key": "value"}] },
    { "input": [3.0, [1, 2, 3]] }
  ],
  "assert_2": [
    { "input": [10.0, 0.0] },
    { "input": [5.0, 0] },
    { "input": [2.0, 0.0] },
    { "input": [1.0, 0] },
    { "input": [3.0, 0.0] }
  ],
  "assert_0,assert_1": [
    { "input": ["not_a_number", "also_not_a_number"] },
    { "input": [None, None] },
    { "input": [True, False] },
    { "input": [{"key": "value"}, [1, 2, 3]] },
    { "input": [[1, 2, 3], {"key": "value"}] }
  ],
  "assert_0,assert_2": [
    { "input": ["not_a_number", 0.0] },
    { "input": [None, 0] },
    { "input": [True, 0.0] },
    { "input": [{"key": "value"}, 0] },
    { "input": [[1, 2, 3], 0.0] }
  ]
}
----------------------------------------
'''

MBPP_DIRECT_EXAMPLE = '''
Method Name:unique_sorted(values)
Problem Description:
"""
Return a sorted tuple of unique integers from the input list.
assert unique_sorted([3, 1, 2, 3, 2]) == (1, 2, 3)
"""
def unique_sorted(values):

    assert isinstance(values, list), "invalid inputs"  # $_CONTRACT_$
    assert all(isinstance(v, int) for v in values), "invalid inputs"  # $_CONTRACT_$
    return tuple(sorted(set(values)))
    
Contract List:
assert_0: assert isinstance(values, list), "invalid inputs"
assert_1: assert all(isinstance(v, int) for v in values), "invalid inputs"

<think>
I will declare input `values` as a Value type, then encode each Python assert as a Bool predicate C0–C1. Basic structure ensures the input is a list while contract predicates model the assertion semantics.
</think>
```json
{
  "assert_1": [
    { "input": [[1, 2, "three", 4]] },
    { "input": [[1, 2.5, 3, 4]] },
    { "input": [[1, True, 3, 4]] },
    { "input": [[1, None, 3, 4]] },
    { "input": [[1, [2], 3, 4]] }
  ],
  "assert_0,assert_1": [
    { "input": ["not_a_list"] },
    { "input": [42] },
    { "input": [{"key": "value"}] },
    { "input": [None] },
    { "input": [(1, 2, 3)] }
  ]
}
```
----------------------------------------
'''

########################################################################################################################
# functionality specification

FUNCTIONALITY_SPECIFICATION = """
You are an expert program analyst.

I will provide:
{header_fields}

Your task is:
- Generate additional test cases that **fully satisfy all assertion conditions in the Contract List**.
– Before emitting any JSON, write a very short chain-of-thought wrapped in <think>…</think> (3–4 sentences) explaining your overall functional testing strategy.**
– All inputs must be valid according to the given contracts; do not include any inputs that would trigger an assertion failure.
- Focus on **testing the core functionality**, not input validation or invalid inputs.
- Each test case must be valid and should help **evaluate the correctness of the main logic** of the function.

Design exactly **one test case for each of the following categories**:
1. boundary_and_edge_case — inputs at the edge of valid ranges (e.g., empty list, minimal valid nesting, only spaces, etc.)
2. complex_corner_case — rare or subtle combinations of valid inputs that may stress internal state or sequencing logic
3. performance_stress_case — large, deeply nested, or computationally heavy but still valid input strings
4. logic_coverage — inputs designed to trigger unusual or less commonly used logical paths
5. functional_path_coverage — inputs that explicitly activate specific internal condition paths (e.g., appending to results, skipping whitespace, etc.)

JSON Rules (STRICT)
- **Absolutely NO comments** (`// …` or `# …`) and no trailing commas.
- Use JSON literals only: `null` (not `None`), `true/false` (not `True/False`).
- Do not output tuples; use lists `[...]` only.
- input: the **list of arguments** to pass to the function that would trigger the assertion failure.

Each test case must include the following fields:
- category: one of ['boundary_and_edge_case', 'complex_corner_case', 'performance_stress_case', 'logic_coverage', 'functional_path_coverage']
- input: a list containing the single argument to the function (must be a valid string that satisfies all contract assertions)
"""

OUTPUT_INSTRUCTION_FUNCTIONALITY = """
----------------------------------------
**Before emitting the JSON object, write a very short `<think>…</think>` block (3–4 sentences) with your overall strategy.**
Respond in structured JSON format, grouped by each category. Provide exactly one test case per category.
Each category must include:
- "input": a list of valid arguments to be passed to the function (must satisfy all assertions)
Each test case must strictly follow the ```json ...``` format as shown below.

### Implementation Guidelines
<think>
...
</think>

```json
{
  "boundary_and_edge_case": {
    "input": [...]
  },
  "complex_corner_case": {
    "input": [...]
  },
  "performance_stress_case": {
    "input": [...]
  },
  "logic_coverage": {
    "input": [...]
  },
  "functional_path_coverage": {
    "input": [...]
  }
}
```
----------------------------------------
"""

FUNCTIONALITY_SPECIFICATION = FUNCTIONALITY_SPECIFICATION.format(
  header_fields="""
- Method Name: the name of the function to test.
- Problem Description: a natural language description of what the function is supposed to do, including its expected behavior, input constraints (as assertions), and a reference implementation.
- Contract List: a list of input validation conditions written as assertions that enforce type, range, and structural constraints before executing the main logic.
  """
)
########################################################################################################################
# FS: functionality specification, CS: contracts specification
# FT: functionality test case, CT: contracts test case

# code generation instruction
CODE_GENERATION_CS = """
You are an expert program analyst.
I will provide:
  - Method Name: the name of the function to test.
  - Problem Description: a one-sentence description of what the function is supposed to do, followed by one or more example assertions.

Your task is:
  1. Read the problem description carefully and infer appropriate arguments for the function.
  2. Write a correct implementation that:
    - Satisfies the described behavior
    - Passes all provided examples
    - If the problem includes input constraints, you may enforce them using assert statements.
  3. Do not change the function name.

**Output** 
  - Return ONLY the code block. Do not include any other text or explanation.
  ```
"""

CODE_GENERATION_CT = """
You are an expert program analyst.

I will provide:
  - Method Name: the name of the function to implement.
  - Problem Description: a one-sentence description of what the function is supposed to do.
  - Functionality Test Cases: valid examples that the function must pass in problem description.
  - Contract Test Cases: invalid inputs that must be rejected using appropriate input validation logic (e.g., assert statements).

Your task is:
  1. Carefully read the problem description.
  2. Analyze the functionality test cases to understand the expected behavior.
  3. Analyze the contract test cases to infer input constraints that must be enforced.
  4. Write a correct implementation that:
    - Passes all functionality test cases.
    - Rejects all contract test cases by raising an AssertionError.
    - Enforces input constraints using assert statements or precondition checks.
  5. Do not change the function name.
  6. Do not return test code or any explanation.

**Output**
  - Return ONLY the code block. Do not include any other text or explanation.
"""

########################################################################################################################
# code refinement instruction
CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CS = """
You are an expert program analyst.

I will provide:
  - Method Name: the name of the function to test.
  - Problem Description: a short description of what the function is supposed to do.
  - Code: the original function implementation.
  - Constraints: one or more natural language constraints that must be enforced before the main logic runs.

Your task is:
1. Carefully read the natural language constraints.
2. Modify the provided function code by inserting appropriate input-validation logic that enforces all given constraints.
  - If a constraint can be checked at runtime, use Python `assert` statements.
  - If a constraint requires logic beyond `assert`, implement additional conditionals or pre-checks as needed.
  - **If there are multiple constraints, implement them in the exact order they are given (0, 1, 2, ...).**
3. Do not change the function name.
4. Do not alter any behavior unrelated to the constraints.
5. Ensure the final code satisfies both the original description and the added constraints.

Return only the updated code inside a ```json fenced code block.
"""

CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CT = """
You are an expert program analyst.

I will provide:
  - Method Name: the name of the function to test.
  - Problem Description: a short description of what the function is supposed to do.
  - Code: the original function implementation.
  - Contract Test Cases: one or more example inputs that violate expected constraints. These test cases trigger assertion errors and should not be accepted by a correct implementation.

Your task is:
1. Carefully analyze the provided contract test cases and infer the underlying input constraints they are testing.
2. Modify the provided function code by inserting appropriate input-validation logic that rejects these invalid inputs.
  - If a constraint can be checked at runtime, use Python `assert` statements to enforce it.
  - If a constraint requires logic beyond `assert`, implement additional conditionals or pre-checks as needed.
  - **If multiple violations are implied, handle each case explicitly and in the order they appear.**
3. Do not change the function name.
4. Do not alter any behavior unrelated to enforcing the inferred constraints.
5. Ensure the final code passes the valid examples and raises `AssertionError` for all provided contract test cases.

Return only the updated code inside a ```json fenced code block.
"""

OUTPUT_INSTRUCTION_CODE_GENERATION = """
----------------------------------------
**Before emitting the JSON object, write a very short `<think>…</think>` block (maximum 2 sentences, no more than 30 words) describing your strategy.**
Then, you must return a valid JSON object containing the Python code inside the `"code"` field.
**The JSON block is mandatory — even if you're unsure, you must always produce code. Never omit it.**

### Output Example
<think>
I will parse the example assertions to infer argument types and constraints. Then I implement the logic to satisfy all examples.
</think>

```json
{
  "code": '''
  ...
  '''
}
```
----------------------------------------
"""


########################################################################################################################
# grammar instruction
LONG_ADT_BASE_TEMPLATE = """
(set-logic ALL)

; ==== CANONICAL PYTHON-LIKE ADT (DO NOT MODIFY) ====
; This is helper ADT for Python-like ADT.
(declare-datatypes ((Value 0)) (
  ((IntVal (ival Int))
   (FloatVal (fval Real))
   (StrVal (sval String))
   (BoolVal (bval Bool))
   (Nil)
   (Cons (head Value) (tail Value)))
))
(define-fun IsList ((v Value)) Bool (or (is-Nil v) (is-Cons v)))
(define-fun-rec list_all_numeric ((v Value)) Bool
  (ite (is-Nil v) true
    (ite (is-Cons v)
      (and (or (is-IntVal (head v)) (is-FloatVal (head v)))
           (list_all_numeric (tail v)))
      false)))
(define-fun-rec list_nonempty ((v Value)) Bool (ite (is-Cons v) true false))
(define-fun-rec length ((v Value)) Int
  (ite (is-Nil v) 0 (ite (is-Cons v) (+ 1 (length (tail v))) 0)))
(define-fun-rec any_numeric ((v Value)) Bool
  (ite (is-Nil v) false
    (ite (is-Cons v)
      (or (or (is-IntVal (head v)) (is-FloatVal (head v)))
          (any_numeric (tail v)))
      false)))
(define-fun-rec any_nonnumeric ((v Value)) Bool
  (ite (is-Nil v) false
    (ite (is-Cons v)
      (or (and (not (is-IntVal (head v))) (not (is-FloatVal (head v))))
          (any_nonnumeric (tail v)))
      false)))

; Python list-ness separate from structural list (used for isinstance(list))
(declare-fun PyList (Value) Bool)

(define-fun-rec has-value ((x Value) (lst Value)) Bool
  (ite (is-Nil lst) false
    (ite (is-Cons lst)
      (or (= x (head lst)) (has-value x (tail lst)))
      false)))

; numeric predicates
(define-fun is_numeric ((x Value)) Bool
  (or (is-IntVal x) (is-FloatVal x)))

(define-fun is_nonzero_numeric ((x Value)) Bool
  (or (and (is-IntVal x) (not (= (ival x) 0)))
      (and (is-FloatVal x) (not (= (fval x) 0.0)))))

; additional useful predicates
(define-fun is_positive_numeric ((x Value)) Bool
  (or (and (is-IntVal x) (> (ival x) 0))
      (and (is-FloatVal x) (> (fval x) 0.0))))

(define-fun is_negative_numeric ((x Value)) Bool
  (or (and (is-IntVal x) (< (ival x) 0))
      (and (is-FloatVal x) (< (fval x) 0.0))))

(define-fun-rec list_length_ge ((lst Value) (n Int)) Bool
  (ite (>= n 0)
    (ite (is-Nil lst) (= n 0)
      (ite (is-Cons lst) (list_length_ge (tail lst) (- n 1))
        false))
    false))

(define-fun-rec list_all_positive ((lst Value)) Bool
  (ite (is-Nil lst) true
    (ite (is-Cons lst)
      (and (is_positive_numeric (head lst))
           (list_all_positive (tail lst)))
      false)))

(define-fun-rec list_contains ((lst Value) (elem Value)) Bool
  (ite (is-Nil lst) false
    (ite (is-Cons lst)
      (or (= (head lst) elem) (list_contains (tail lst) elem))
      false)))

(define-fun is_empty_list ((lst Value)) Bool
  (is-Nil lst))

(define-fun is_single_element_list ((lst Value)) Bool
  (and (is-Cons lst) (is-Nil (tail lst))))

(define-fun-rec list_all_strings ((lst Value)) Bool
  (ite (is-Nil lst) true
    (ite (is-Cons lst)
      (and (is-StrVal (head lst))
           (list_all_strings (tail lst)))
      false)))

(define-fun-rec list_all_bools ((lst Value)) Bool
  (ite (is-Nil lst) true
    (ite (is-Cons lst)
      (and (is-BoolVal (head lst))
           (list_all_bools (tail lst)))
      false)))

; === ADD HELPER FUNCTIONS HERE ===
<<HELPER_FUNCTIONS>>

; === Inputs ===
<<INPUT>>

; === BASIC STRUCTURE ===
<<BASIC_STRUCTURE>>

; === Contract predicates ===
<<CONTRACT_DEFS>>

; === COMBINATION ===
<<COMBINATION>>

(check-sat)
(get-model)
"""

LONG_GRAMMAR_OUTPUT_INSTRUCTION = """
I will provide:
- Method Name: the function name to analyze
- Problem Description: natural language description of function behavior and constraints
- Contract List: input validation assertions that enforce type, range, and structural constraints

Your tasks:
1) **CRITICAL**: Ensure ALL inputs satisfy basic structural requirements for program execution:
   - Correct ADT shapes and types
   - Valid list structures and nesting
   - Appropriate numeric/string/boolean constraints
2) **Generate ONE SMT-LIB v2 base template** containing:
   - (a) The canonical ADT block exactly as provided
   - (b) Input declarations: `(declare-const <param> Value)` for each parameter
   - (c) Basic structure assertions for executability (apply selectively based on testing needs):
       • Lists: `(assert (IsList <param>))` - only when testing list-specific contracts
       • Numerics: `(assert (or (is-IntVal <param>) (is-FloatVal <param>)))` - only when testing numeric contracts
       • Strings: `(assert (is-StrVal <param>))` - only when testing string contracts
       • Booleans: `(assert (is-BoolVal <param>))` - only when testing boolean contracts
   - (d) Placeholder slots: 
       • `<<HELPER_FUNCTIONS>>` - Additional custom helper functions if needed (usually empty)
       • `<<BASIC_STRUCTURE>>` - Basic type/structural constraints for program execution
       • `<<CONTRACT_DEFS>>` - Contract predicate definitions (C0, C1, C2, ...)
       • `<<COMBINATION>>` - Test scenario combinations
3) **Define contract predicates**: For each Python assert, create a named Bool predicate Ck that exactly matches the assertion semantics
4) **Ensure mathematical precision**: All SMT expressions must be syntactically correct and semantically equivalent to Python assertions
5) Cover ALL combinations: singles, pairs, triples, … up to “all violated”.
6) **Output format**: Return a JSON object with the specified structure
"""

ADT_BASE_TEMPLATE = """
(set-logic ALL)

; ==== CANONICAL PYTHON-LIKE ADT (DO NOT MODIFY) ====
(declare-datatypes ((Value 0)) (
  ((IntVal (ival Int))
   (FloatVal (fval Real))
   (StrVal (sval String))
   (BoolVal (bval Bool))
   (Nil)
   (Cons (head Value) (tail Value)))
))

; === ADD HELPER FUNCTIONS HERE ===
<<HELPER_FUNCTIONS>>

; === Inputs ===
<<INPUT>>

; === BASIC STRUCTURE ===
<<BASIC_STRUCTURE>>

; === Contract predicates ===
<<CONTRACT_DEFS>>

; === COMBINATION ===
<<COMBINATION>>

(check-sat)
(get-model)
"""

GRAMMAR_ASSERT_SPECIFICATION = """
You are an expert program analyst specializing in formal verification and SMT-LIB v2 specification.

Your task is to analyze Python code with input-validation assertions (contracts) and generate a comprehensive SMT-LIB v2 specification that:
1. Models each contract as a named Boolean predicate (C0, C1, C2, ...)
2. Ensures program executability through proper ADT constraints
3. Provides a reusable template for generating test scenarios
4. Supports systematic contract violation testing

Focus on creating precise, mathematically sound SMT specifications that accurately represent Python assertion semantics.

{STRICT_RULES}
"""

STRICT_RULES = """
STRICT RULES (concise, extensible)
- ADT: Declare the Value ADT exactly once. Additional constructors MAY be added if needed.
- Inputs: Use (declare-const <param> Value) by default. Primitive sorts only when strictly necessary, consistently.
- Testers: Use only is-<Ctor> (e.g., is-FloatVal v); never (is FloatVal v).
- Selector safety: Always guard ival/fval/sval/bval with testers or Safe* helpers; wrap with ite if needed. NEVER use selectors directly on Value.
- Regex: Use str.in.re with (str.to.re "..."). Do NOT use re.unit, re.full-match, anchors (^, $), or indexed forms. Always guard with is-StrVal or SafeS.
- Let bindings: Parallel only. Bindings in the same let MUST NOT depend on each other. Nest lets when dependencies are required.
- Naming: Let-bound names must be descriptive and non-shadowing.
- Executability vs contracts: BASIC_STRUCTURE holds invariants required in all cases. Ck only contains test-specific properties.
- Contracts & combination: Each Ck is a standalone Bool, defined before use, satisfiable even when others are negated. COMBINATION may only reference Ck atoms (and/or negations).
- Assert granularity: One Python assert statement maps to exactly one Ck. Even if it contains conjunctions (and/or), keep it as a single predicate unless the original code had multiple assert statements. Do NOT split a single assert into multiple Ck.
- Recursion: Any self- or mutual-recursive function MUST use define-fun-rec with a base case and decreasing measure.
- Recursion guards: Recursive calls must be guarded with ite so terms disappear when guards are false (negation-safe).
- Output hygiene: No comments, no unused symbols, definitions precede use. Ck names must be stable (C0, C1, ...).
- Orthogonality: Each Ck must be independently satisfiable and violable while others hold. If inherent overlaps exist, list them in unsat_exclusions.
- Factor invariants out: Shared invariants (types, list-shape, caps) MUST live in BASIC_STRUCTURE only.
- Negation-friendly form: Guards first, then property. Avoid definitions that collapse to UNSAT under negation.
- Domain partitioning: When multiple contracts constrain the same dimension (e.g., length vs charset), design them as orthogonal. Never let one imply the other.
- Explicit safety caps: Length/magnitude/depth caps live ONLY in BASIC_STRUCTURE.
- Regex independence: Charset restrictions go to BASIC_STRUCTURE. Ck may add prefixes/suffixes/length only.
- Lists & selectors: All selectors guarded; IsList, ListLen, list_all_numeric in BASIC_STRUCTURE, not repeated per Ck.
"""
GRAMMAR_ASSERT_OUTPUT_INSTRUCTION = """
I will provide:
- Method Name: the function name to analyze
- Problem Description: description of function behavior and constraints
- Contract List: Python assert statements enforcing type, range, or structure

Your tasks:
1) Ensure all inputs satisfy execution requirements:
   - Correct ADT shapes and types
   - Valid list structures and nesting
   - Proper numeric/string/boolean constraints
   - Use define-fun-rec for recursive helpers (e.g., list_all_numeric, length)
2) Generate ONE SMT-LIB v2 base template including:
   - ADT definition
   - Required helper functions
   - Input declarations (declare-const <param> Value)
   - Basic structure assertions
   - Contract predicate definitions (C0, C1, ...)
3) Each Python assert → exactly one Ck Bool predicate with equivalent semantics.
4) Expressions must be mathematically precise and syntactically valid SMT-LIB.
5) Cover all combinations: singles, pairs, triples, up to all violated.
6) Output: JSON object in the specified format, with NO comments inside helper_functions, basic_structure, inputs, or contract_defs.

Before emitting:
1) Map each assert statement to one Ck. Do NOT split a single assert into multiple Ck.
2) Move invariants shared by all asserts to BASIC_STRUCTURE.
3) For each Ck, both (Ck ∧ others) and (~Ck ∧ others) must be SAT unless inherently UNSAT, in which case record in unsat_exclusions.
4) Ensure Ck never references another Cj.
5) Keep regex vs length orthogonal.
6) Guards must eliminate recursive calls under negation (negation-safe).

Base Template:
{ADT_BASE_TEMPLATE}

Output Format:
{ADT_OUTPUT_FORMAT}
----------------------------------------
"""

ADT_ASSERT_OUTPUT_FORMAT = """
<think>
Briefly explain your approach (2-3 sentences). Example: "I will analyze the Python assertions and translate them into precise SMT-LIB predicates while maintaining program executability constraints."
</think>
```json
{
  "helper_functions": "<<HELPER_FUNCTIONS>>",
  "basic_structure": "<<BASIC_STRUCTURE>>",
  "inputs": "(declare-const <param1> Value)\\n(declare-const <param2> Value)\\n...",
  "contract_defs": {
    "assert_0": "(define-fun C0 () Bool <...>)",
    "assert_1": "(define-fun C1 () Bool <...>)",
    "assert_2": "(define-fun C2 () Bool <...>)",
    ...
  }
}
```
----------------------------------------
"""

GRAMMAR_FUNCTIONALITY_SPECIFICATION = """
You are an expert program analyst specializing in formal verification and SMT-LIB v2 specification.

Goal
- Produce SMT-LIB v2 specifications that generate functionally valid inputs (i.e., all contracts hold) for three scenarios:
  1) boundary_and_edge_case — hit contract-implied minima/maxima or exact anchors while staying valid.
  2) complex_corner_case — realize rare but valid combinations (two+ independent tight constraints and/or uncommon structural/value patterns).
  3) performance_stress_case — maximize workload (size/nesting/pattern complexity) under explicit safety caps, while satisfying all contracts.
"""


HUMANEVAL_ASSERT_ADT_EXAMPLE = '''
Method: safe_divide
Problem Description:
def safe_divide(a, b):
    """Return a / b if b != 0 else None.
    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(5, 0)
    None
    """

    assert isinstance(a, (int, float)), "invalid inputs"  # $_CONTRACT_$
    assert isinstance(b, (int, float)), "invalid inputs"  # $_CONTRACT_$
    assert b != 0, "invalid inputs"  # $_CONTRACT_$

    return a / b

Contract List:
assert_0: assert isinstance(a, (int, float)), "invalid inputs"
assert_1: assert isinstance(b, (int, float)), "invalid inputs"
assert_2: assert b != 0, "invalid inputs"

<think>
I will declare inputs `a` and `b` as Value types, then encode each Python assert as a Bool predicate C0–C2. Basic structure constraints ensure executability while contract predicates model the assertion semantics.
</think>
```json
{
  "helper_functions": "(define-fun is-IntVal ((x Value)) Bool (is-IntVal x))\\n(define-fun is-FloatVal ((x Value)) Bool (is-FloatVal x))\\n(define-fun ival ((x Value)) Int (ival x))\\n(define-fun fval ((x Value)) Real (fval x))",
  "basic_structure": "(assert (or (is-IntVal a) (is-FloatVal a)))\\n(assert (or (is-IntVal b) (is-FloatVal b)))",
  "inputs": "(declare-const a Value)\\n(declare-const b Value)",
  "contract_defs": {
    "assert_0": "(define-fun C0 () Bool (or (is-IntVal a) (is-FloatVal a)))",
    "assert_1": "(define-fun C1 () Bool (or (is-IntVal b) (is-FloatVal b)))",
    "assert_2": "(define-fun C2 () Bool (or (and (is-IntVal b) (not (= (ival b) 0))) (and (is-FloatVal b) (not (= (fval b) 0.0)))))"
  }
}
```
----------------------------------------
'''

MBPP_ASSERT_ADT_EXAMPLE = '''
Method Name:unique_sorted(values)
Problem Description:
"""
Return a sorted tuple of unique integers from the input list.
assert unique_sorted([3, 1, 2, 3, 2]) == (1, 2, 3)
"""
def unique_sorted(values):

    assert isinstance(values, list), "invalid inputs"  # $_CONTRACT_$
    assert all(isinstance(v, int) for v in values), "invalid inputs"  # $_CONTRACT_$
    return tuple(sorted(set(values)))
    
Contract List:
assert_0: assert isinstance(values, list), "invalid inputs"
assert_1: assert all(isinstance(v, int) for v in values), "invalid inputs"

<think>
I will declare input `values` as a Value type, then encode each Python assert as a Bool predicate C0–C1. Basic structure ensures the input is a list while contract predicates model the assertion semantics.
</think>
```json
{
  "helper_functions": "(define-fun-rec list_all_ints ((v Value)) Bool\\n  (ite (is-Nil v) true\\n    (ite (is-Cons v)\\n      (and (is-IntVal (head v)) (list_all_ints (tail v)))\\n      false)))",
  "basic_structure": "(assert (IsList values))",
  "inputs": "(declare-const values Value)",
  "contract_defs": {
    "assert_0": "(define-fun C0 () Bool (IsList values))",
    "assert_1": "(define-fun C1 () Bool (list_all_ints values))"
  }
}
```
----------------------------------------
'''



########################################################################################################################
# main function

def instruction_template(which, **kwargs):
  # For gpt-4o-mini instructions to make contracts natural language
  if which == "HUMANEVAL_MASK_STRING":
    return HUMANEVAL_MASK_STRING, OUTPUT_INSTRUCTION_MASK_STRING
  elif which == "MBPP_MASK_STRING":
    return MBPP_MASK_STRING, OUTPUT_INSTRUCTION_MASK_STRING
  elif which == "INDIVIDUAL_MASK_STRING":
    return INDIVIDUAL_MASK_STRING, OUTPUT_INSTRUCTION_INDIVIDUAL_MASK_STRING
  
  # test case instruction
  elif which == "INSTRUCTION_10":
    return INSTRUCTION_10, OUTPUT_INSTRUCTION_10
  elif which == "EX-INSTRUCTION_10":
    return INSTRUCTION_10, OUTPUT_EX_INSTRUCTION_10

  elif which == "FUNCTIONALITY_SPECIFICATION":
    return FUNCTIONALITY_SPECIFICATION, OUTPUT_INSTRUCTION_FUNCTIONALITY

  elif which == "ASSERT_SPECIFICATION":
    return ASSERT_SPECIFICATION, OUTPUT_INSTRUCTION_ASSERTIONS
  
  elif which == "MULTI_ASSERT_SPECIFICATION":
    return MULTI_ASSERT_SPECIFICATION, MULTI_OUTPUT_INSTRUCTION_ASSERTIONS
  elif which == "MULTI_ASSERT_SPECIFICATION_humaneval": # ONE SHOT
    return MULTI_ASSERT_SPECIFICATION, MULTI_OUTPUT_INSTRUCTION_ASSERTIONS + HUMANEVAL_DIRECT_EXAMPLE
  elif which == "MULTI_ASSERT_SPECIFICATION_mbpp": # ONE SHOT
    return MULTI_ASSERT_SPECIFICATION, MULTI_OUTPUT_INSTRUCTION_ASSERTIONS + MBPP_DIRECT_EXAMPLE
  
  elif which == "GRAMMAR_ASSERT_SPECIFICATION":
    return GRAMMAR_ASSERT_SPECIFICATION.format(STRICT_RULES=STRICT_RULES), GRAMMAR_ASSERT_OUTPUT_INSTRUCTION.format(ADT_BASE_TEMPLATE=ADT_BASE_TEMPLATE, ADT_OUTPUT_FORMAT=ADT_ASSERT_OUTPUT_FORMAT)
  elif which == "GRAMMAR_ASSERT_SPECIFICATION_humaneval": # ONE SHOT
    return GRAMMAR_ASSERT_SPECIFICATION.format(STRICT_RULES=STRICT_RULES), GRAMMAR_ASSERT_OUTPUT_INSTRUCTION.format(ADT_BASE_TEMPLATE=ADT_BASE_TEMPLATE, ADT_OUTPUT_FORMAT=ADT_ASSERT_OUTPUT_FORMAT) + HUMANEVAL_ASSERT_ADT_EXAMPLE
  elif which == "GRAMMAR_ASSERT_SPECIFICATION_mbpp": # ONE SHOT
    return GRAMMAR_ASSERT_SPECIFICATION.format(STRICT_RULES=STRICT_RULES), GRAMMAR_ASSERT_OUTPUT_INSTRUCTION.format(ADT_BASE_TEMPLATE=ADT_BASE_TEMPLATE, ADT_OUTPUT_FORMAT=ADT_ASSERT_OUTPUT_FORMAT) + MBPP_ASSERT_ADT_EXAMPLE
  
  
  
  # code generation instruction
  elif which == "CODE_GENERATION_CS":
    return CODE_GENERATION_CS, OUTPUT_INSTRUCTION_CODE_GENERATION
  elif which == "CODE_GENERATION_CT":
    return CODE_GENERATION_CT, OUTPUT_INSTRUCTION_CODE_GENERATION

  # code refinement instruction
  elif which == "CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CS":
    return CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CS, OUTPUT_INSTRUCTION_CODE_GENERATION
  elif which == "CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CT":
    return CODE_REFINEMENT_WITH_INSTRUCTIONS_FC_CT, OUTPUT_INSTRUCTION_CODE_GENERATION
  else:
    raise ValueError(f"Unknown instruction type: {which}")