# DO LARGE LANGUAGE MODELS RESPECT CON-TRACTS? EVALUATING AND ENFORCING CONTRACT ADHERENCE IN CODE GENERATION

📖 [Paper](https://~~~~~)

This repository support the paper "DO LARGE LANGUAGE MODELS RESPECT CON-TRACTS? EVALUATING AND ENFORCING CONTRACT ADHERENCE IN CODE GENERATION".


## Updates
- 10/10/2025

## Abstract
Prevailing code generation benchmarks, such as HumanEval+ and MBPP+, primarily evaluate large language models (LLMs) with *pass@k* on functional correctness using well-formed inputs.
However, they ignore a crucial aspect of real-world software: adherence to *contracts*—the preconditions and validity constraints that dictate how ill-formed inputs must be rejected.

This critical oversight means that existing benchmarks fail to measure, and models consequently fail to generate, truly robust and reliable code snippets.
We introduce **PACT**, a program assessment and contract-adherence evaluation framework, to bridge this gap.
PACT is the first framework designed to systematically evaluate and enhance contract-adherence in LLM-generated code snippets alongside functional correctness.
PACT's contributions are threefold:
First, it provides a comprehensive test-suite corpus focused on contract violations, extending HumanEval+ and MBPP+.
Second, it enables a systematic analysis of code generation under varied prompting conditions. This analysis demonstrates that augmenting prompts with contract-violating test cases significantly enhance a model's ability to respect contracts compared to using contract description alone.
Finally, it introduces novel metrics to rigorously quantify contract adherence in both test generation and code generation.
By revealing critical errors that conventional benchmarks overlook, PACT provides the rigorous and interpretable metrics
to evaluate the robustness of LLM-generated code snippets in both functionality and contract-adherence.

## About PACT
![Full Picture](figures/example.png)

**PACT** is a novel framework for evaluating and enhancing contract adherence in LLM-generated code.
Unlike traditional benchmarks that measure only *functional correctness* through *pass@k* on well-formed inputs, PACT systematically assesses whether generated programs respect preconditions and input validation rules (contracts).

It extends HumanEval+ and MBPP+ with contract-violating test suites, enabling a more complete view of model robustness.
Through **SMT-based test generation** and **contract-adherence metrics**, PACT offers the first principled framework for measuring how reliably LLMs enforce contracts in code generation.

The above figure is a running example of PACT with an Example-Augmented Specification (EAS) prompt, which integrates Contract Specification (CS) and Contract-Violating Test cases (CVTs) to enforce contract-aware code generation.

---
### 🔹 How PACT Works
PACT operates in **two main stages** to evaluate and enhance **contract adherence** in LLM-generated code.

### **Step 1: Contract-Violating Test Generation**
- PACT begins by translating **natural-language contract descriptions** (e.g., input bounds, type constraints, error-handling rules) into a **formal representation** using **Algebraic Data Types (ADT)**.  
- The resulting ADT schema is passed to an **SMT solver (Z3)**, which systematically generates **Contract-Violating Test Cases (CVTs)**.  
- These CVTs are designed to **violate one or more contracts** while ensuring all remaining conditions stay valid, allowing precise testing of boundary behavior.  
- This stage ensures that generated test cases are **logically consistent**, **semantically valid**, and directly tied to the intended specification.  
- The quality of generated CVTs is evaluated using **two novel metrics proposed by PACT**:  
  - **Assert Violation Coverage (AVC)** – measures how many contracts are successfully tested by violations.  
  - **Target Specificity (TS)** – measures how accurately each test case targets the intended contract violations.  

### **Step 2: Contract-Aware Code Generation**
- The generated **CVTs** are used to evaluate and guide LLMs during code generation.  
- PACT compares model behavior under two prompting settings:  
  - **Contract Specification (CS)** – includes only functional and natural-language contract descriptions.  
  - **Example-Augmented Specification (EAS)** – augments the CS prompt with the **CVTs** from Step 1, giving explicit examples of invalid inputs.  
- By contrasting these two settings, PACT reveals how concrete violation examples improve a model’s ability to **detect and handle contract-violating test cases**, leading to more reliable and contract-aware code generation.
- The generated code snippets are then evaluated using **three novel contract-adherence metrics proposed by PACT**:  
  - **Assert Violation Coverage (AVC)** – *same metric as in Step 1*, but here it measures how effectively the **generated code** detects and rejects contract-violating inputs (runtime enforcement).
  - **Assertion Alignment Recall (AAR)** – measures how many ground-truth contracts are correctly implemented.  
  - **Assertion Alignment Precision (AAP)** – measures how accurate and relevant the generated assertions are.  
---

### **🚀 PACT Achievements**
✅ **Introduces contract awareness as a new evaluation perspective** – PACT shifts the focus from pure functional correctness to whether LLMs understand and respect *contracts* such as preconditions and input constraints.  
✅ **Proposes novel metrics for measuring contract adherence** – PACT defines rigorous, interpretable metrics (AVC, TS, AAR, AAP) to quantify how well models enforce these contracts.  
✅ **Reveals how reliably LLMs follow contracts in practice** – Through systematic experiments on HumanEval+ and MBPP+, PACT demonstrates that models often overlook contractual rules, and quantifies their improvements when guided by contract-violating test cases.

---

### Results of PACT on Contract-Adherence Benchmarks
<b>HumanEval+</b></h3>

| Model          | Mode |  pass@1 ↑ |   AVC ↑   |   AAR ↑   |   AAP ↑   |   AVG ↑   |
| :------------- | :--- | :-------: | :-------: | :-------: | :-------: | :-------: |
| **gemma-3**    | CS   | **84.41** |   24.85   |   11.41   |   14.04   |   32.79   |
|                | EAS  |   82.94   | **91.02** | **28.07** | **27.77** | **57.45** |
| **DeepSeek**   | CS   | **73.78** |   44.12   |   15.65   |   16.97   |   37.63   |
|                | EAS  |   71.77   | **79.29** | **27.62** | **28.01** | **51.67** |
| **Qwen3**      | CS   | **78.92** |   28.04   |   13.17   |   22.55   |   35.67   |
|                | EAS  |   77.83   | **87.81** | **31.53** | **36.09** | **58.31** |
| **Phi-4-plus** | CS   | **72.23** |   52.91   |   18.78   | **21.09** |   41.25   |
|                | EAS  |   67.08   | **69.50** | **21.33** |   20.06   | **44.49** |

<b>MBPP+</b></h3>

| Model          | Mode |  pass@1 ↑ |   AVC ↑   |   AAR ↑   |   AAP ↑   |   AVG ↑   |
| :------------- | :--- | :-------: | :-------: | :-------: | :-------: | :-------: |
| **gemma-3**    | CS   |   78.56   |   57.99   |   17.50   |   17.93   |   41.49   |
|                | EAS  | **78.60** | **95.57** | **32.29** | **31.82** | **59.57** |
| **DeepSeek**   | CS   | **62.53** |   64.20   |   17.59   |   17.57   |   40.47   |
|                | EAS  |   60.15   | **86.70** | **28.23** | **27.94** | **45.47** |
| **Qwen3**      | CS   |   72.41   |   70.86   |   21.09   |   22.99   |   46.84   |
|                | EAS  | **72.63** | **94.85** | **31.54** | **32.30** | **57.83** |
| **Phi-4-plus** | CS   | **64.89** |   67.33   |   24.26   |   24.65   |   45.28   |
|                | EAS  |   63.76   | **74.88** | **29.20** | **28.95** | **49.20** |


---

## Installation
~~~shell
conda env create --file setting/environment.yaml
conda activate PACT
~~~
Clone the repository and set up the environment.

## Getting Started
The following scripts guide you through running PACT step by step:

### **1️⃣ CVTs Genration**
~~~shell
### STEP 1: Generation
sh ./scripts/generation_gpt/gpt_main.sh

### STEP 2: Parsing
#### Default
sh ./scripts/utils/inference_parsing.sh

### STEP 3: SMT Solver
sh ./scripts/utils/grammar_smt_tool.sh

### STEP 4: Evaluation (pass@k)
sh ./scripts/utils/evaluation_test_case_pass_k.sh

### STEP 5: Evaluation (our metric)
sh ./scripts/utils/evaluation_test_case_pass_k_for_grammar.sh
~~~
This stage executes the full **contract-violating test-case (CVT) generation and evaluation pipeline**.  
Each script performs the following functions:  
- **Generation:** Produces initial test cases based on natural-language contract descriptions.  
- **Parsing:** Converts the raw model outputs into a standardized JSON format.  
- **SMT Solver:** Validates the logical consistency of generated cases using the **Z3 solver**.  
- **Evaluation (pass@k):** Measures baseline functional correctness of the generated tests.  
- **Evaluation (our metric):** Computes **AVC** and **TS**, the proposed metrics for evaluating the quality of contract-violating test cases.  

Each script in this stage supports **detailed configuration options** that can be adjusted within the corresponding shell files.


### **2️⃣ Code Generation**
~~~shell
### STEP 1: Generation
sh ./scripts/generation_test_case_or_code_generation/main.sh

### STEP 2: Evaluation (code generation)
sh ./scripts/utils/evaluation_code_generation.sh
~~~
This stage executes the **contract-aware code generation and evaluation pipeline** using the CVTs generated in Step 1.  
Each script performs the following functions:  
- **Generation:** Produces code solutions under two prompting settings:
  - **Contract Specification (CS)** (baseline)
  - **Example-Augmented Specification (EAS)** (augmented with CVTs).  
- **Evaluation:** Assesses generated code for both functionality and contract adherence using the proposed metrics: **AVC**, **AAR**, and **AAP**, which measure how effectively the model enforces and aligns with contracts.  

Each script in this stage supports **detailed configuration options** that can be adjusted within the corresponding shell files.