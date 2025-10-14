#!/usr/bin/env bash
##################################################################################################
### **Default parameters**
ENV_FILE="${ENV_FILE:-./api_key.env}" # Load API KEY from api_key.env
if [ -f "$ENV_FILE" ]; then
  set -o allexport
  . "$ENV_FILE"
  set +o allexport
fi
: "${OPEN_API_KEY:?Set OPEN_API_KEY in $ENV_FILE}"

##################################################################################################
### **Custom parameters**
TEST_TYPE="GRAMMAR_ASSERT_SPECIFICATION"  # This parameter is used to determine the task to be executed.
# Components: "GRAMMAR_ASSERT_SPECIFICATION" "MULTI_ASSERT_SPECIFICATION"

DATASET="mbpp" # This parameter is used to determine the dataset to be executed.
# Components: "humaneval", "mbpp"

MODEL_NAMES="o4-mini" # This parameter is used to determine the model to be executed.
# Default

NUM_SAMPLES=1

TEMPERATURE=1 # This parameter is used to determine the temperature of the model.
# Components: 0.7, 1.0

##################################################################################################
if [ "$TEST_TYPE" = "GRAMMAR_ASSERT_SPECIFICATION" ]; then
    OUTPUT_DIR="../../code/output_gpt/original/${MODEL_NAMES}/grammar_assert_specification"
    USE_INSTRUCTIONS="GRAMMAR_ASSERT_SPECIFICATION"
elif [ "$TEST_TYPE" = "MULTI_ASSERT_SPECIFICATION" ]; then
    OUTPUT_DIR="../../code/output_gpt/original/${MODEL_NAMES}/multi_assert_specification"
    USE_INSTRUCTIONS="MULTI_ASSERT_SPECIFICATION"
else
    echo "Invalid TEST_TYPE: $TEST_TYPE (must be 'functionality' or 'contracts')"
    exit 1
fi

echo "Using dataset: $DATASET"
echo "Using test type: $TEST_TYPE"
echo "==============================="
echo "Using instruction: $USE_INSTRUCTIONS"
echo "Running model: $MODEL_NAMES"

LOG_DIR="../../code/output_gpt/original/$(echo "${MODEL_NAMES}" | tr '[:upper:]' '[:lower:]')/$(echo "${TEST_TYPE}" | tr '[:upper:]' '[:lower:]')"
LOG_FILE="${LOG_DIR}/$(echo "${DATASET}" | tr '[:upper:]' '[:lower:]')_$(echo "${MODEL_NAMES}" | tr '[:upper:]' '[:lower:]')_$(echo "${TEST_TYPE}" | tr '[:upper:]' '[:lower:]').log"

mkdir -p "$LOG_DIR"
> "$LOG_FILE"

python ../../code/gpt_main.py \
    --dataset "$DATASET" \
    --use_instruction "$USE_INSTRUCTIONS" \
    --model "$MODEL_NAMES" \
    --num_samples $NUM_SAMPLES \
    --temperature $TEMPERATURE \
    --output_dir $OUTPUT_DIR \
    --open_api_key $OPEN_API_KEY \
    > "$LOG_FILE"