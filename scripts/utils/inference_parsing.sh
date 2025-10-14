#!/usr/bin/env bash
# This is a script for inference parsing.
##################################################################################################
### **Default parameters**
TEST_CASE_TYPES=(
  "multi_assert_specification"
  )

DATASETS=(
  "humaneval" 
  "mbpp"
  )
##################################################################################################
### **Custom parameters**
MODEL_NAMES=( # Add model names here. This means what model to use for parsing.
  "o4-mini"
)

##################################################################################################
for DATASET in "${DATASETS[@]}"; do
  for TEST_CASE_TYPE in "${TEST_CASE_TYPES[@]}"; do
    for MODEL_NAME in "${MODEL_NAMES[@]}"; do
      echo "Parsing Model: $MODEL_NAME | Dataset: $DATASET | TestCase: $TEST_CASE_TYPE"
      python ../../code/utils/inference_parsing.py \
        --dataset_type "$DATASET" \
        --model_name  "$MODEL_NAME" \
        --test_case_type "$TEST_CASE_TYPE"
    done
  done
done