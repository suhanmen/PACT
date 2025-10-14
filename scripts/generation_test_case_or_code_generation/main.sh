#!/bin/bash
# This is a script for generation test case or code generation.
##################################################################################################
### **Default parameters**
DATASETS=(
  #"humaneval"
  #"mbpp"
  "total"
)

# use hyper parameters
BATCH_SIZE=10
NUM_SAMPLES=1
MAX_LENGTH=4096
USE_QLORA=False
##################################################################################################
### **Custom parameters**
export CUDA_VISIBLE_DEVICES=${1:-1} # This means which GPU to use.
echo "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"

TASK='code_generation' # This parameter is used to determine the task to be executed.
# Default

MODEL_NAMES=(
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
    "Qwen/Qwen3-14B"
    "microsoft/Phi-4-reasoning-plus"
    "google/gemma-3-12b-it"
)
 
CODE_GEN_MODE="SFT" 
# Default

SKIP_COMPLETED=True # This parameter is used to determine whether to skip the completed test cases.
# Components: "True", "False"

SAMPLE_N="False" # This parameter is used to determine whether to sample the test cases.
# Components: "True", "False"
##################################################################################################
if [ "$TASK" = "code_generation" ]; then
  USE_INSTRUCTIONS=(
    "CODE_GENERATION_CS"
    "CODE_GENERATION_CT"
  )
fi

[ -d log ] || mkdir log

for DATASET in "${DATASETS[@]}"; do
  echo "==============================="
  echo "Using dataset: $DATASET"
  for USE_INSTRUCTION in "${USE_INSTRUCTIONS[@]}"; do
    echo "==============================="
    echo "Using instruction: $USE_INSTRUCTION"

    MAX_NEW_TOKENS=1024 # If 0, it means max_new_Tokens = max_length - input_length. This is automatically set by the input length.

    for MODEL_NAME in "${MODEL_NAMES[@]}"; do
      MODEL_SHORT_NAME=$(basename "$MODEL_NAME")
      echo "Running model: $MODEL_NAME"
      mkdir -p log/${DATASET}_${MODEL_SHORT_NAME}
      python ../../code/TG_CG_main.py \
        --dataset "$DATASET" \
        --model_name "$MODEL_NAME" \
        --batch_size $BATCH_SIZE \
        --num_samples $NUM_SAMPLES \
        --max_length $MAX_LENGTH \
        --max_new_tokens $MAX_NEW_TOKENS \
        --use_instruction $USE_INSTRUCTION \
        --use_qlora $USE_QLORA \
        --skip_completed $SKIP_COMPLETED \
        --code_gen_mode $CODE_GEN_MODE \
        --sample_n $SAMPLE_N \
        > log/${DATASET}_${MODEL_SHORT_NAME}/${USE_INSTRUCTION}.log 
    done
  done
done