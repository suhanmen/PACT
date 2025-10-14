#!/bin/bash
# This is a script for evaluating the model for code generation.
##################################################################################################
### **Default parameters**
set -euo pipefail
MODES=(
  "code_generation_total_cs"
  "code_generation_total_ct"
)

CODE_GEN_MODE="full"
# Components: "base", "our", "full"

OUR_MODE="SFT"
# Default

USE_NONE_LIST="False" # What to use for task_id?
# Components: "True" (use out_task_id), "False" (use in_task_id)

CONTRACT_TEST_CASE_TYPE="direct"
# Default

CODE_GENERATION_MODEL_NAMES=( ### Add code generation model names here
  "DeepSeek-R1-Distill-Qwen-14B"
  "Qwen3-14B"
  "Phi-4-reasoning-plus" 
  "o4-mini"
  "gemma-3-12b-it"
)
# Components: "DeepSeek", "Qwen", "Phi", "gemma"...

OUTPUT_PATH="../../code/evaluation_code_generation/total/"

HUMAN_EVAL_FUNCTIONALITY_DATASET_PATH="../../data/evalplus-0.1.1/HumanEvalPlus.jsonl"
MBPP_FUNCTIONALITY_DATASET_PATH="../../data/mbppplus-0.2.0/MbppPlus.jsonl"
HUMAN_EVAL_CONTRACTS_DATASET_PATH="../../code/evaluation_test_case_pass_k/humaneval/pre_filtering/multi_assert_specification/o4-mini/o4-mini_all_results.json"
MBPP_CONTRACTS_DATASET_PATH="../../code/evaluation_test_case_pass_k/mbpp/pre_filtering/multi_assert_specification/o4-mini/o4-mini_all_results.json"
##################################################################################################

echo "------------------------------------------------------------"
for MODE in "${MODES[@]}"; do
  for MODEL_NAME in "${CODE_GENERATION_MODEL_NAMES[@]}"; do
    if [ "$CODE_GEN_MODE" == "full" ]; then
      if [ "$MODE" == "code_generation_total_cs" ]; then
        TOTAL_EVAL_CODE_GENERATION_MODEL_PATH="../../code/output_full/total/inference/${MODEL_NAME}/code_generation_cs/generated_step_all.jsonl" 
      else
        TOTAL_EVAL_CODE_GENERATION_MODEL_PATH="../../code/output_full/total/inference/${MODEL_NAME}/code_generation_ct/generated_step_all.jsonl" 
      fi
      TOTAL_EVAL_CODE_GENERATION_MODEL_PATH_STR=$TOTAL_EVAL_CODE_GENERATION_MODEL_PATH

    if [ "$CODE_GEN_MODE" == "full" ]; then
      OUT_DIR="${OUTPUT_PATH}${MODE}-${CONTRACT_TEST_CASE_TYPE}-${CODE_GEN_MODE}/${MODEL_NAME}/"
    fi
    
    mkdir -p "$OUT_DIR"
    echo "→ MODE=$MODE  DATASET=total "
    echo "→ MODEL_NAME: $MODEL_NAME"
    echo "=== Evaluating ==="
    echo "    → output_dir: $OUT_DIR"
    echo "    → modeldir : $TOTAL_EVAL_CODE_GENERATION_MODEL_PATH"


    echo $TOTAL_EVAL_CODE_GENERATION_MODEL_PATH
    python ../../code/utils/evaluation_code_generation.py \
        --code_generation_model_path "$TOTAL_EVAL_CODE_GENERATION_MODEL_PATH_STR" \
        --code_generation_model_name "$MODEL_NAME" \
        --humaneval_functionality_dataset_path "$HUMAN_EVAL_FUNCTIONALITY_DATASET_PATH" \
        --mbpp_functionality_dataset_path "$MBPP_FUNCTIONALITY_DATASET_PATH" \
        --humaneval_contracts_dataset_path "$HUMAN_EVAL_CONTRACTS_DATASET_PATH" \
        --mbpp_contracts_dataset_path "$MBPP_CONTRACTS_DATASET_PATH" \
        --output_path "$OUT_DIR" \
        --mode "$MODE" \
        --use_None_list "$USE_NONE_LIST" \
        --contract_test_case_type "$CONTRACT_TEST_CASE_TYPE"
    echo "\n✅ All evaluations finished."
  done
done
