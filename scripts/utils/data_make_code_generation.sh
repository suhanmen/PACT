#!/bin/bash
# This is a script for evaluating the model for code generation.
##################################################################################################
### **Default parameters**

set -euo pipefail

MODE=(
  "CODE_GENERATION_CS" 
  "CODE_GENERATION_CT"
)

DATASET=(
  "humaneval"
  "mbpp"
)
# Components: "humaneval", "mbpp"

CODE_GENERATION_MODEL_NAMES=(
  "o4-mini"
)
# Components: "o4-mini"
# Output path will be set per MODE/MODEL inside the loop
##################################################################################################
for DATASET in "${DATASET[@]}"; do
  for MODE in "${MODE[@]}"; do
    for MODEL_NAME in "${CODE_GENERATION_MODEL_NAMES[@]}"; do
      
      if [ "$MODEL_NAME" == "o4-mini" ]; then
        TEST_CASE_DATA_PATH="../../code/evaluation_test_case_pass_k_for_grammar/${DATASET}/pre_filtering/grammar_assert_specification/${MODEL_NAME}/${MODEL_NAME}_contract_check_results.json"
      else
        TEST_CASE_DATA_PATH="../../code/evaluation_test_case_pass_k_for_grammar/${DATASET}/pre_filtering/grammar_assert_specification/${MODEL_NAME}/${MODEL_NAME%%-*}-RL_contract_check_results.json"
      fi

      OUTPUT_DIR="../../data/code_generation/${DATASET}/${MODE}/${MODEL_NAME}"
      mkdir -p "$OUTPUT_DIR"

      python ../../code/utils/data_make_code_generation.py \
          --test_case_data_path "$TEST_CASE_DATA_PATH" \
          --mode "$MODE" \
          --dataset "$DATASET" \
          --model_name "$MODEL_NAME" \
          --output_path "$OUTPUT_DIR"
    done
  done
done

