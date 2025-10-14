# Generation_gpt
## if assert_specification
### STEP 1: Generation
sh ./generation_gpt/gpt_main.sh

### STEP 2: Parsing
sh ./utils/inference_parsing.sh

### STEP 3: Evaluation
sh ./utils/evaluation_test_case_pass_k.sh

### STEP 4: After Quality
sh ./generation_gpt/after_quality.sh

### STEP 5: Train/Valid split
sh ./utils/train_valid_split.sh


## else grammar_assert_speficivation
### STEP 1: Generation
sh ./generation_test_case_or_code_generation/main.sh

### STEP 2: Parsing + SMT solver
sh ./utils/grammar_smt_tool.sh

### STEP 3: Evaluation
sh ./utils/evaluation_test_case_k_for_grammar.sh

### STEP 5: Train/Valid split
sh ./utils/train_valid_split.sh


---
# Generation test case (LLM Direct method)
### STEP 1: Generation
sh ./generation_test_case_or_code_generation/main.sh

### STEP 2: Parsing
#### Default
sh ./utils/inference_parsing.sh
#### ADT Base method
sh. ./utils/grammar_smt_tool.sh

### STEP 3: Evaluation (pass@k)
sh ./utils/evaluation_test_case_pass_k.sh

### STEP 4: Evaluation (our metric)
sh ./utils/evaluation_test_case_pass_k_for_grammar.sh

---
# Generation code (LLM Direct method)
### STEP 1: Generation
sh ./generation_test_case_or_code_generation/main.sh

### STEP 2: Evaluation (code generation)
sh ./utils/evaluation_code_generation.sh
