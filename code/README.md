## File Descriptions

### `inference_parsing.py`
**Purpose**: Parses LLM outputs and generates JSON and CSV results
- Processes LLM-generated outputs and converts them into structured formats
- Handles different model outputs (GPT, custom models) with appropriate parsing logic
- Generates CSV files for analysis (requires CSV viewer extension for proper display)
- Supports both contract and function test case types
- Includes data cleaning and validation functions

### `model_setting.py`
**Purpose**: Configuration file for model loading and QLoRA setup
- Defines BitsAndBytes configuration for 4-bit quantization
- Sets up LoRA (Low-Rank Adaptation) configuration for efficient fine-tuning
- Configures target modules for attention layers (q_proj, v_proj)
- Provides centralized model configuration settings

### `Instruction.py`
**Purpose**: Collection of instruction templates for model interactions
- Contains natural language instruction templates for different tasks
- Includes specialized prompts for contract analysis and function testing
- Provides structured output formats for various evaluation scenarios
- Supports both HumanEval and MBPP dataset formats
- Contains mask strings for different instruction types

### `evaluation_code_generation.py`
**Purpose**: Evaluates code generation quality using pass@k metrics
- Implements pass@k evaluation for generated code
- Executes Python code safely with timeout protection
- Handles various error types and edge cases
- Provides comprehensive evaluation metrics for code quality
- Supports multiple evaluation scenarios and datasets

### `after_quality.py`
**Purpose**: Quality assessment and filtering of test cases
- Compares ground truth code outputs with model-generated test case outputs
- Filters test cases based on two criteria:
  1. Ground truth code produces assertions
  2. Ground truth code produces assertions AND model output is error-free
- Currently supports GPT test cases only
- Generates filtered datasets for further processing

### `evaluation_test_case_pass_k.py`
**Purpose**: Evaluates test case quality using pass@k metrics
- Executes generated test cases against both ground truth and model code
- Calculates pass@k results for test case effectiveness
- Stores results in pass_output directory
- Handles various test case formats and execution scenarios
- Provides comprehensive evaluation metrics

### `train_valid_split.py`
**Purpose**: Splits test case datasets into training and validation sets
- Divides test cases into 9:1 ratio (train:validation)
- Currently supports GPT test cases only
- Generates split summary CSV with statistics
- Creates separate files for train, validation, and test sets
- Maintains data integrity during splitting process

### `load_data.py`
**Purpose**: Data loading utilities for different datasets
- Supports multiple dataset types (HumanEval, MBPP variants)
- Defines section categories for test case classification
- Provides standardized data loading interfaces
- Handles dataset-specific configurations and formats

### `reward_contract.py`
**Purpose**: Contract-based reward calculation for test cases
- Implements contract validation and scoring mechanisms
- Analyzes assertion coverage and effectiveness
- Provides metrics for contract-based evaluation
- Supports complex contract validation scenarios

### `reward_function.py`
**Purpose**: Functionality-based reward calculation
- Implements coverage-based reward mechanisms
- Evaluates test case effectiveness using line and branch coverage
- Provides timeout protection for test execution
- Generates detailed reward metrics for optimization

### `evaluation_code_generation.py`
**Purpose**: Comprehensive code generation evaluation with reward calculation
- Evaluates generated code quality using functionality and contract metrics
- Implements EvaluationRewarder class for multi-metric scoring
- Calculates AAR (Assertion Alignment Recall) and AAP (Assertion Alignment Precision)
- Supports resumable evaluation with progress saving
- Provides detailed compilation statistics and per-task metrics
- Handles both HumanEval and MBPP datasets with contract checking

### `evaluation_test_case_pass_k_for_grammar.py`
**Purpose**: Grammar-based test case evaluation with SMT solver integration
- Evaluates test cases generated using grammar and SMT solvers
- Implements GrammarRewarder class for contract-based metrics
- Supports one-by-one contract checking with combination testing
- Calculates AVC (Assert Violation Coverage) and TS (Test Strength) metrics
- Handles contract combinations and violation scenarios
- Generates detailed pass@k results for grammar-generated test cases

### `grammar_smt_tool_gpt_format.py`
**Purpose**: Grammar and SMT solver tool for test case generation
- Implements GrammarTool for parsing LLM outputs in various formats
- Implements SMTTool for Z3 solver integration
- Generates test cases using SMT solvers from grammar specifications
- Supports contract combinations and constraint satisfaction
- Handles timeout and hard timeout scenarios
- Exports test cases in JSON and TXT formats
- Includes comprehensive logging and statistics generation
- Supports both GPT and open LLM output formats

###  `data_concat.py`
**Purpose**: Data concatenation utility for code generation datasets
- Concatenates HumanEval and MBPP datasets
- Creates unified training, validation, and test splits
- Filters data based on CODE_GENERATION_CT availability
- Supports both CODE_GENERATION_CS and CODE_GENERATION_CT modes
- Automatically handles train/valid/test splitting with sklearn

### `data_label_check.py`
**Purpose**: Data label verification and quality checking
- Verifies canonical solution correctness for both datasets
- Checks functionality test case execution on ground truth code
- Validates contract test case behavior (AssertionError checking)
- Computes functionality and contract scores for data quality
- Supports both "in_contracts" and "no_contracts" modes
- Generates detailed JSON reports with failure analysis

### `data_make_code_generation.py`
**Purpose**: Code generation dataset creation from test cases
- Creates CODE_GENERATION_CS and CODE_GENERATION_CT datasets
- Integrates contract test cases with code generation prompts
- Handles parameter ordering and test case instruction formatting
- Implements test case pruning and deduplication
- Supports contract key normalization and aggregation
- Creates aligned datasets for training and evaluation
- Includes ground truth verification for contract test cases

### `data_train_valid_split.py`
**Purpose**: Dataset splitting utility for training and validation
- Splits datasets into train, validation, and test sets
- Supports cross-dataset test set creation (HumanEval ↔ MBPP)
- Generates summary CSV with split statistics
- Configurable validation ratio and random seed
- Handles both grammar_assert_specification and other test case types

## Additional Notes
- Most evaluation scripts include timeout protection and error handling
- The codebase supports both contract-based and functionality-based testing approaches
- Multiple evaluation metrics are available for comprehensive assessment
- The system is designed to handle various model outputs and dataset formats
- Error handling and logging are implemented throughout the evaluation pipeline
- Grammar-SMT integration enables automated test case generation from formal specifications
- Comprehensive data preprocessing and quality checking utilities ensure dataset integrity 