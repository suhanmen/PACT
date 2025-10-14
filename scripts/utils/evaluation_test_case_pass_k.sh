#!/usr/bin/env bash
# This is a script for evaluating the model for test case.
##################################################################################################
### **Custom parameters**
set -euo pipefail

MODE="pre_filtering" # This means initial test case filtering.
# Components: "pre_filtering", "post_filtering"

INFERENCE_MODE="gpt" # This means what model to create test case.
# Components: "base", "ours", "gpt", "humaneval_test" (original dataset), "mbpp_test" (original dataset)

DATASET=(
  "humaneval" 
  "mbpp"
) 
# Components: "humaneval", "mbpp"

# Add test case model names here
PRE_BASE_MODELS=(
  DeepSeek-R1-Distill-Qwen-14B
  Phi-4-reasoning-plus
  Qwen3-14B
  gemma-3-12b-it
)

PRE_GPT_MODELS=(
  o4-mini
)

##################################################################################################
### **Default parameters**
MODELS_BASE_DIR="../../data/models/" # path to the models
OUTPUT_PATH="../../code/evaluation_test_case_pass_k/" # path to the output

pre_tag="-generated_step_all" # tag for the test case
post_tag="_pre_filtering_results_filtered" # tag for the pre-filtering test case
##################################################################################################

for DATASET in "${DATASET[@]}"; do
  CUSTOM_TESTCASES_FILES=()  # reset per dataset
  pre_filtering_ground_path="../../code/output_base/${DATASET}/parsing_data/" # path to the base test case
  pre_filtering_ours_ground_path="../../code/output_ours/${DATASET}/parsing_data/" # path to the our test case
  pre_filtering_gpt_ground_path="../../code/output_gpt/${DATASET}/parsing_data/" # path to the gpt test case


  post_filtering_ground_path="../../code/evaluation_test_case_pass_k/${DATASET}/pre_filtering/" # path to the pre-filtering test case


  if [[ $MODE == "pre_filtering" ]]; then
      MODEL_NAMES=(ground_truth)
  else  
      if [[ $DATASET == "humaneval" ]]; then
          MODEL_NAMES=(chatgpt_temp_0.0 gpt-4_temp_0.0)
      else  
          MODEL_NAMES=(gpt-3.5-turbo_temp_0.0 gpt-4-1106-preview_temp_0.0)
      fi
  fi

  echo "→ MODE=$MODE  DATASET=$DATASET  INFERENCE_MODE=$INFERENCE_MODE"
  echo "→ MODEL_NAMES: ${MODEL_NAMES[*]}"

  add_file() {
      local f=$1
      [[ -f $f ]] && CUSTOM_TESTCASES_FILES+=("$f") || \
          echo "⚠️  (missing, skipped) $f" >&2
  }

  case "${MODE}" in
    pre_filtering)
      case "${DATASET}" in
        humaneval)
          case "${INFERENCE_MODE}" in
            base)
              for MODEL in "${PRE_BASE_MODELS[@]}"; do
                add_file "${pre_filtering_ground_path}multi_assert_specification/${MODEL}${pre_tag}.json"
              done
              ;;
            gpt)
              for MODEL in "${PRE_GPT_MODELS[@]}"; do
                add_file "${pre_filtering_gpt_ground_path}multi_assert_specification/${MODEL}${pre_tag}.json"
              done
              ;;
          esac
          ;;
        mbpp)
          case "${INFERENCE_MODE}" in
            base)
              for MODEL in "${PRE_BASE_MODELS[@]}"; do
                add_file "${pre_filtering_ground_path}multi_assert_specification/${MODEL}${pre_tag}.json"
              done
              ;;
            gpt)
              for MODEL in "${PRE_GPT_MODELS[@]}"; do
                add_file "${pre_filtering_gpt_ground_path}multi_assert_specification/${MODEL}${pre_tag}.json"
              done
              ;;
          esac
          ;;
      esac
      ;;

    post_filtering)
      case "${DATASET}" in
        humaneval)
          case "${INFERENCE_MODE}" in
            base)
              for MODEL in "${POST_BASE_MODELS[@]}"; do
                add_file "${post_filtering_ground_path}assert_specification/${MODEL}/${MODEL}${post_tag}.json"
                add_file "${post_filtering_ground_path}functionality_specification/${MODEL}/${MODEL}${post_tag}.json"
              done
              ;;
            gpt)
              for MODEL in "${PRE_GPT_MODELS[@]}"; do
                add_file "${post_filtering_ground_path}assert_specification/${MODEL}/${MODEL}${post_tag}.json"
                add_file "${post_filtering_ground_path}functionality_specification/${MODEL}/${MODEL}${post_tag}.json"
              done
              ;;
            humaneval_test)
              add_file "../../data/evalplus-0.1.1/HumanEvalPlus.jsonl"
              ;;
          esac
          ;;
        mbpp)
          case "${INFERENCE_MODE}" in
            base)
              for MODEL in "${POST_BASE_MODELS[@]}"; do
                add_file "${post_filtering_ground_path}assert_specification/${MODEL}/${MODEL}${post_tag}.json"
                add_file "${post_filtering_ground_path}functionality_specification/${MODEL}/${MODEL}${post_tag}.json"
              done
              ;;
            gpt)
              for MODEL in "${PRE_GPT_MODELS[@]}"; do
                add_file "${post_filtering_ground_path}assert_specification/${MODEL}/${MODEL}${post_tag}.json"
                add_file "${post_filtering_ground_path}functionality_specification/${MODEL}/${MODEL}${post_tag}.json"
              done
              ;;
              mbpp_test)
              add_file "../../data/mbppplus-0.2.0/MbppPlus.jsonl"
              ;;
          esac
          ;;
      esac
      ;;

  esac

  if [[ ${#CUSTOM_TESTCASES_FILES[@]} -eq 0 ]]; then
      echo "❌ No test‑case JSONs resolved – check your MODE/DATASET/INFERENCE_MODE combo" >&2
      exit 1
  fi

  echo "→ ${#CUSTOM_TESTCASES_FILES[@]} testcase JSON(s) resolved:"
  printf '   • %s\n' "${CUSTOM_TESTCASES_FILES[@]}"

  echo "------------------------------------------------------------"
  echo "Running evaluation_model.py ..."
  echo "------------------------------------------------------------"

  for TEST_CASES_JSON in "${CUSTOM_TESTCASES_FILES[@]}"; do
      if [[ "${TEST_CASES_JSON}" == *.jsonl ]]; then
          BASENAME=$(basename "$TEST_CASES_JSON" .jsonl)
          if [[ $BASENAME == *"HumanEvalPlus"* ]]; then
              DATASET_SEG="humaneval"
          elif [[ $BASENAME == *"MbppPlus"* ]]; then
              DATASET_SEG="mbpp"
          fi
      else
          BASENAME=$(basename "$TEST_CASES_JSON" .json)
          DATASET_SEG=$(echo "$TEST_CASES_JSON" | awk -F/ '{print tolower($5)}')
      fi  
      
      OUT_DIR="${OUTPUT_PATH}${DATASET_SEG}/"
      MODELS_DIR="${MODELS_BASE_DIR}${DATASET_SEG}/"

      mkdir -p "$OUT_DIR"
      echo
      echo "=== Evaluating: $BASENAME ==="
      echo "    → output_dir: $OUT_DIR"
      echo "    → modeldir : $MODELS_DIR"

      python ../../code/utils/evaluation_test_case_pass_k.py \
          --models_base_dir "$MODELS_DIR" \
          --model_names "${MODEL_NAMES[@]}" \
          --test_cases_json "$TEST_CASES_JSON" \
          --output_path "$OUT_DIR" \
          --mode "$MODE"
  done

  echo "\n✅ All evaluations finished."
done