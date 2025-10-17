# Do large language models respect contracts? Evaluating and enforcing contract-adherence in code generation

<p align="center">
  <a href="https://github.com/suhanmen/PACT/stargazers">
    <img src="https://img.shields.io/github/stars/suhanmen/PACT?style=social" alt="GitHub Repo stars">
  </a>
  <a href="https://github.com/suhanmen/PACT/commits/main">
    <img src="https://img.shields.io/github/last-commit/suhanmen/PACT" alt="GitHub last commit">
  </a>
  <a href="https://github.com/suhanmen/PACT/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/suhanmen/PACT?color=orange" alt="GitHub contributors">
  </a>
</p>

<div align="center">
    <a href="https://arxiv.org/abs/2510.12047"><b>Paper Link</b>📖</a>
</div><br>


## 📰 News
- 📢 NEW! **"Do large language models respect contracts? Evaluating and enforcing contract-adherence in code generation"** is now on arXiv. (Oct 14, 2025)
- 📢 NEW! The official **PACT** framework has been released on GitHub. (Oct 14, 2025)

## 🔍 Motivation
<p align="center">
  <img src="figures/motivation.png" alt="Motivation Figure" width="60%">
</p>

Large Language Models can generate working code—but can they generate safe code? **PACT** goes beyond pass@k accuracy to ask a deeper question: “Does the model respect the rules of the program?” By testing how models handle invalid inputs and preconditions, PACT reveals hidden weaknesses in current benchmarks and provides a new standard for contract-aware code evaluation.

## ✨ About PACT
**PACT** is a novel framework for evaluating and enhancing contract adherence in LLM-generated code.
Unlike traditional benchmarks that measure only *functional correctness* through *pass@k* on well-formed inputs, PACT systematically assesses whether generated programs respect preconditions and input validation rules (contracts).

It extends HumanEval+ and MBPP+ with contract-violating test suites, enabling a more complete view of model robustness.
Through **SMT-based test generation** and **contract-adherence metrics**, PACT offers the first principled framework for measuring how reliably LLMs enforce contracts in code generation.


The above figure is a running example of PACT with an Example-Augmented Specification (EAS) prompt, which integrates Contract Specification (CS) and contract-violating test cases (CVTs) to enforce contract-aware code generation.

## 🚀 What makes PACT valuable?
✅ **Introduces contract awareness as a new evaluation perspective** – PACT shifts the focus from pure *functional correctness* to whether LLMs understand and respect **contracts**,  such as preconditions and input constraints.  

✅ **Defines novel and interpretable metrics for contract adherence** – PACT introduces four new metrics — **AVC**, **TS**, **AAR**, and **AAP** —  to rigorously measure how well models detect and enforce contracts in both test generation and code generation.  

✅ **Reveals hidden weaknesses in current benchmarks** – Through systematic experiments on **HumanEval+** and **MBPP+**, PACT uncovers that many “functionally correct” programs fail to enforce basic contracts, and demonstrates how contract-violating test cases substantially improve robustness.


## 📈 Results
Our comprehensive evaluation across 4 LLMs (Gemma-3, DeepSeek-R1, Qwen-3, Phi-4-plus) on HumanEval+ and MBPP+ reveals several key findings:

* **Contract-aware test generation** – PACT’s two-stage LLM + SMT solver pipeline produced logically consistent contract-violating test cases (CVTs), achieving an average +12.8 pp improvement in Target Specificity (TS) over direct LLM generation while maintaining high Assert Violation Coverage (AVC). This demonstrates the precision of PACT’s targeted violation generation.

* **Prompting strategy matters** – Augmenting the Contract Specification (CS) prompt with CVTs (Example-Augmented Specification, EAS) boosted contract adherence metrics by +33.7 pp (AVC), +11.6 pp (AAR), and +9.9 pp (AAP) on average. Concrete examples help LLMs explicitly learn how to enforce contracts.

* **Trade-off with functional correctness** – While EAS substantially improves contract robustness, it induces a slight drop in pass@1 for well-formed inputs. This reflects a core tension between functional accuracy and robust contract enforcement.

For detailed quantitative results and case analyses, please refer to our paper.


## 🛠️ Setup

### Requirements
~~~shell
conda env create --file setting/environment.yaml
conda activate PACT
~~~
Clone the repository and set up the environment.

### Datasets
* `HumanEvalPlus.jsonl` — A benchmark dataset consisting of 164 programming problems, used end-to-end for CVT generation and code-generation evaluation. Version **v0.1.1** was used in our experiments.
* `MBPPPlus.jsonl` — A benchmark dataset consisting of 378 programming problems, used end-to-end for CVT generation and code-generation evaluation. Version **v0.2.0** was used in our experiments.


## ⚡ Quickstart
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


## 🔖 Citation
```
@misc{lim2025largelanguagemodelsrespect,
      title={Do Large Language Models Respect Contracts? Evaluating and Enforcing Contract-Adherence in Code Generation}, 
      author={Soohan Lim and Joonghyuk Hahn and Hyunwoo Park and Sang-Ki Ko and Yo-Sub Han},
      year={2025},
      eprint={2510.12047},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2510.12047}, 
}
```