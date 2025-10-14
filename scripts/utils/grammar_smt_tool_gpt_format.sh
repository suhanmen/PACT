#!/usr/bin/env bash
##################################################################################################
DATASET=(
    "humaneval"
    "mbpp"
)

GRAMMAR_FILE_TYPE="gpt"
# Default: "gpt"

TRAIN_MODE="SFT" # This means SFT or RL
# Default: "SFT"

INFERENCE_GPT_MODEL="o4-mini"
# Default: "o4-mini"

if [ "$GRAMMAR_FILE_TYPE" == "gpt" ]; then
    INFERENCE_MODEL=(
        $INFERENCE_GPT_MODEL
    )
else
    # if GRAMMAR_FILE_TYPE is base, then use the following models
    INFERENCE_MODEL=(
        "None"
    )
fi

TIMEOUT=30
NUM_SOLUTIONS=5
##################################################################################################
for DATASET in "${DATASET[@]}"; do
    for MODEL in "${INFERENCE_MODEL[@]}"; do
    if [ "$MODEL" == "o4-mini" ]; then
        TEST_CASE_OUTPUT_PATH_MODEL="o4-mini"
    else
        echo "Invalid MODEL"
        exit 1
    fi

    if [ "$GRAMMAR_FILE_TYPE" == "gpt" ]; then
        GRAMMAR_FILE="../../code/output_${GRAMMAR_FILE_TYPE}/original/${INFERENCE_GPT_MODEL}/grammar_assert_specification/${DATASET}_${INFERENCE_GPT_MODEL}_sft.jsonl"
        OUTPUT_PATH="../../code/output_${GRAMMAR_FILE_TYPE}/${DATASET}/parsing_data/grammar_assert_specification/${INFERENCE_GPT_MODEL}/${INFERENCE_GPT_MODEL}-parsing.json"
        TEST_CASE_OUTPUT_PATH="../../code/output_${GRAMMAR_FILE_TYPE}/${DATASET}/after_quality/grammar_assert_specification/${INFERENCE_GPT_MODEL}/"
    else
        echo "Invalid GRAMMAR_FILE_TYPE"
        exit 1
    fi

    TEST_CASE_OUTPUT_PATH_MODEL="${MODEL}"

    python ../../code/utils/grammar_smt_tool_gpt_format.py \
    --model $MODEL \
    --grammar_file $GRAMMAR_FILE \
    --output_path $OUTPUT_PATH \
    --test_case_output_path $TEST_CASE_OUTPUT_PATH \
    --test_case_output_path_model $TEST_CASE_OUTPUT_PATH_MODEL \
    --solver "z3" \
    --timeout $TIMEOUT \
    --num_solutions $NUM_SOLUTIONS
    done
done