import json
import subprocess
import tempfile
import os
import sys
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path
import argparse
import pdb
from z3 import *
from z3 import is_true, Or
import datetime
import csv
from fractions import Fraction
import inspect
import time 
import re
import multiprocessing
from Instruction import ADT_BASE_TEMPLATE
import ast

class GrammarTool:
    def __init__(self):
        pass
    
    def extract_grammar_result(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract JSON part from model output safely (Open LLM format)"""
        outputs = data.get('outputs', [])
        output_str = outputs[0]
        try:
            think_split = output_str.split('</think>')
            after_think = think_split[1]
        except:
            print(f"{data['task_id']}-> No </think> found")
            after_think = output_str

        #########################################################################
        # Find JSON block | this is use for open llm model
        json_str = ""
        
        # First, find ```json block
        json_start = after_think.find('```json')
        if json_start != -1:
            json_block = after_think[json_start + 7:]  # 7: len('```json')
            json_end = json_block.find('```')
            if json_end != -1:
                json_str = json_block[:json_end].strip()
        
        # If no ```json block, find ``` block
        if not json_str:
            json_start = after_think.find('```')
            if json_start != -1:
                json_block = after_think[json_start + 4:]  # 4: len('```')
                json_end = json_block.find('```')
                if json_end != -1:
                    json_str = json_block[:json_end].strip()
        
        # If no JSON string, find helper_functions
        if not json_str:
            if "helper_functions" in after_think:
                helper_idx = after_think.find("helper_functions")
                if helper_idx != -1:
                    brace_start = after_think.rfind('{', 0, helper_idx)
                    brace_end = after_think.rfind('}')
                    if brace_start != -1 and brace_end != -1 and brace_end > brace_start:
                        json_str = after_think[brace_start:brace_end+1].strip()
                    else:
                        json_end = after_think.rfind('}')
                        json_str = after_think[:json_end+1].strip()
        
        if not json_str:
            pass
        
        #########################################################################
        # JSON LOAD
        # Before JSON parsing, handle escape characters
        try:
            # First, try normal JSON parsing
            parsed_json = json.loads(json_str)
        except json.JSONDecodeError as e:
            # If JSON parsing fails, try to correct escape characters
            try:
                # Replace backslashes with double backslashes
                corrected_json = json_str.replace('\\', '\\\\')
                parsed_json = json.loads(corrected_json)
            except json.JSONDecodeError:
                # If still fails, try more robust correction
                try:
                    # Correct common escape sequences
                    corrected_json = json_str.replace('\\n', '\\\\n').replace('\\t', '\\\\t').replace('\\r', '\\\\r')
                    parsed_json = json.loads(corrected_json)
                except json.JSONDecodeError as final_e:
                    # If still fails, print original error and detailed information
                    print(f"{data['task_id']}-> JSON parsing final failure: {final_e}")
                    parsed_json = None

        if parsed_json is None:
            return None
        else:
            result = {
                "helper_functions": parsed_json.get("helper_functions", ""),
                "basic_structure": parsed_json.get("basic_structure", ""),
                "inputs": parsed_json.get("inputs", ""),
                "contract_defs": parsed_json.get("contract_defs", {}),
            }
            return result
    
    def extract_grammar_result_gpt(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract grammar result from GPT model format"""
       
        try:
            # if gpt model, extract JSON string from grammar.production[0]
            grammar_data = data.get('grammar', {})
            if not grammar_data or not grammar_data[0].get('production'):
                print(f"{data['name']}-> No grammar production found")
                return None
            
            # production string
            production_str = grammar_data[0]['production'][0]
            
            # JSON parsing
            try:
                parsed_json = json.loads(production_str)
            except json.JSONDecodeError as e:
                print(f"{data['name']}-> JSON parsing failure: {e}")
                print(f'"production": {production_str}')
                print("="*50)
                return None
            
            result = {
                "helper_functions": parsed_json.get("helper_functions", ""),
                "basic_structure": parsed_json.get("basic_structure", ""),
                "inputs": parsed_json.get("inputs", ""),
                "contract_defs": parsed_json.get("contract_defs", {}),
            }
            return result
            
        except Exception as e:
            print(f"{data['name']}-> GPT format grammar extraction error: {e}")
            return None
    
    def escape_json_values(s: str) -> str:
        pattern = r'(".*?")\s*:\s*"(.*?)"'
        def replacer(match):
            key = match.group(1)
            value = match.group(2)
            fixed_value = value.replace('"', '\\"')
            return f'{key}: "{fixed_value}"'

        return re.sub(pattern, replacer, s, flags=re.DOTALL)

    def fix_broken_multiline(s: str) -> str:
        return re.sub(r'"\s*\)\s*\\n\s*\(', r'\\n(', s)
    
    def extract_grammar_result_for_reward(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract JSON part from model output safely (Open LLM format)"""
        output_str = data.get("grammar", {})
  
        if '</think>' in output_str:
            think_split = output_str.split('</think>')
            after_think = think_split[1]
        else:
            after_think = output_str
    
        
    def extract_grammar_result_for_reward_sft_rl(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract JSON part from model output safely (Open LLM format)"""
        output_str = data.get("grammar", {})
        if not output_str or not output_str[0].get('production'):
            print(f"{data['name']}-> No grammar production found")
            return None
        
        # production string
        if isinstance(output_str[0]['production'][0], list):
            production_str = output_str[0]['production'][0][0]
        else:
            production_str = output_str[0]['production'][0]

        json_str = ""
        
        # First, find ```json block
        json_start = production_str.find('```json')
        if json_start != -1:
            json_block = production_str[json_start + 7:]  # 7: len('```json')
            json_end = json_block.find('```')
            if json_end != -1:
                json_str = json_block[:json_end].strip()
        
        # If no ```json block, find ``` block
        if not json_str:
            json_start = production_str.find('```')
            if json_start != -1:
                json_block = production_str[json_start + 4:]  # 4: len('```')
                json_end = json_block.find('```')
                if json_end != -1:
                    json_str = json_block[:json_end].strip()
        
        # If no JSON string, find helper_functions
        if not json_str:
            if "helper_functions" in production_str:
                helper_idx = production_str.find("helper_functions")
                if helper_idx != -1:
                    brace_start = production_str.rfind('{', 0, helper_idx)
                    brace_end = production_str.rfind('}')
                    if brace_start != -1 and brace_end != -1 and brace_end > brace_start:
                        json_str = production_str[brace_start:brace_end+1].strip()
                    else:
                        json_end = production_str.rfind('}')
                        json_str = production_str[:json_end+1].strip()

        if not json_str:
            pass
        
        #########################################################################
        # # JSON LOAD
        # # Before JSON parsing, handle escape characters
        # try:
        #     # First, try normal JSON parsing
        #     try:
        #         parsed_json = json.loads(json_str)
        #     except:
        #         corrected_json = json_str.encode('utf-8').decode('unicode_escape')    
        #         parsed_json = json.loads(corrected_json)
                
        # except json.JSONDecodeError as e:
        #     # If JSON parsing fails, try to correct escape characters
        #     try:
        #         # Replace backslashes with double backslashes
        #         corrected_json = json_str.replace('\\', '\\\\')
        #         parsed_json = json.loads(corrected_json)
        #     except json.JSONDecodeError:
        #         # If still fails, try more robust correction
        #         try:
        #             # Correct common escape sequences
        #             corrected_json = json_str.replace('\\n', '\\\\n').replace('\\t', '\\\\t').replace('\\r', '\\\\r')
        #             parsed_json = json.loads(corrected_json)
        #         except json.JSONDecodeError as final_e:
        #             # If still fails, print original error and detailed information
        #             print(f"❌ JSON parsing failed: {final_e}")
        #             parsed_json = None

        # if parsed_json is None:
        #     print(f"{data['name']}-> JSON parsing failed")
        #     return None
        # else:
        #     result = {
        #         "helper_functions": parsed_json.get("helper_functions", ""),
        #         "basic_structure": parsed_json.get("basic_structure", ""),
        #         "inputs": parsed_json.get("inputs", ""),
        #         "contract_defs": parsed_json.get("contract_defs", {}),
        #     }
        #     return result
    
        parsed_json = None
        #try:
        # First, try normal JSON parsing
        try:
            parsed_json = json.loads(json_str)
        except:
            try:
                corrected_json = json_str.encode('utf-8').decode('unicode_escape')    
                parsed_json = json.loads(corrected_json)
               
            except:
                try:
                    fixed = json_str.encode('utf-8').decode('unicode_escape')
                    fixed = self.fix_broken_multiline(fixed)
                    fixed = self.escape_json_values(fixed)
                    parsed_json = json.loads(fixed)
                except:
                    try:
                        cleaned = fixed.replace("\\'", "'").replace('\\"', '"')
                        parsed_json = ast.literal_eval(cleaned)
                    except:
                        print("❌ JSON parsing failed")
                        parsed_json = None
                        
        if parsed_json is None:
            print(f"{data['name']}-> JSON parsing failed")
            return None
         
        result = {
            "helper_functions": parsed_json.get("helper_functions", ""),
            "basic_structure": parsed_json.get("basic_structure", ""),
            "inputs": parsed_json.get("inputs", ""),
            "contract_defs": parsed_json.get("contract_defs", {}),
        }
        return result
    
    def extract_grammar_result_for_reward(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract JSON part from model output safely (Open LLM format)"""
        output_str = data.get("grammar", {})
  
        if '</think>' in output_str:
            think_split = output_str.split('</think>')
            after_think = think_split[1]
        else:
            after_think = output_str

        #########################################################################
        # Find JSON block | this is use for open llm model
        json_str = ""
        
        # First, find ```json block
        json_start = after_think.find('```json')
        if json_start != -1:
            json_block = after_think[json_start + 7:]  # 7: len('```json')
            json_end = json_block.find('```')
            if json_end != -1:
                json_str = json_block[:json_end].strip()
        
        # If no ```json block, find ``` block
        if not json_str:
            json_start = after_think.find('```')
            if json_start != -1:
                json_block = after_think[json_start + 4:]  # 4: len('```')
                json_end = json_block.find('```')
                if json_end != -1:
                    json_str = json_block[:json_end].strip()
        
        # If no JSON string, find helper_functions
        if not json_str:
            if "helper_functions" in after_think:
                helper_idx = after_think.find("helper_functions")
                if helper_idx != -1:
                    brace_start = after_think.rfind('{', 0, helper_idx)
                    brace_end = after_think.rfind('}')
                    if brace_start != -1 and brace_end != -1 and brace_end > brace_start:
                        json_str = after_think[brace_start:brace_end+1].strip()
                    else:
                        json_end = after_think.rfind('}')
                        json_str = after_think[:json_end+1].strip()
        
        if not json_str:
            pass
        
        #########################################################################
        # JSON LOAD
        # Before JSON parsing, handle escape characters
        try:
            # First, try normal JSON parsing
            parsed_json = json.loads(json_str)
        except json.JSONDecodeError as e:
            # If JSON parsing fails, try to correct escape characters
            try:
                # Replace backslashes with double backslashes
                corrected_json = json_str.replace('\\', '\\\\')
                parsed_json = json.loads(corrected_json)
            except json.JSONDecodeError:
                # If still fails, try more robust correction
                try:
                    # Correct common escape sequences
                    corrected_json = json_str.replace('\\n', '\\\\n').replace('\\t', '\\\\t').replace('\\r', '\\\\r')
                    parsed_json = json.loads(corrected_json)
                except json.JSONDecodeError as final_e:
                    # If still fails, print original error and detailed information
                    print(f"JSON parsing final failure: {final_e}")
                    parsed_json = None

        if parsed_json is None:
            return None
        else:
            result = {
                "helper_functions": parsed_json.get("helper_functions", ""),
                "basic_structure": parsed_json.get("basic_structure", ""),
                "inputs": parsed_json.get("inputs", ""),
                "contract_defs": parsed_json.get("contract_defs", {}),
            }
            return result
    
    def parse_grammar_json(self, json_data: Any, model_key: str = None) -> Dict[str, Dict[str, Any]]:
        # check data type
        if isinstance(json_data, list) and model_key == 'o4-mini':
            return self._parse_gpt_format(json_data)
        elif isinstance(json_data, list) and model_key != 'o4-mini':
            return self._parse_SFT_RL_format(json_data, model_key)
        elif isinstance(json_data, dict) and "Setting" in json_data:
            return self._parse_openllm_format(json_data)
        else:
            raise ValueError("Unsupported data type")
    
    def _parse_gpt_format(self, data_list: List[Dict[str, Any]], model_key: str = None) -> Dict[str, Dict[str, Any]]:
        """parse gpt format"""
        result = {}
        
        # # if gpt model, extract model name from file name or use default value
        model_key = "gpt_model"  # or extract from file name
        result[model_key] = {}

        base_template = ADT_BASE_TEMPLATE
        
        for data in data_list:
            task_id = data.get('name')
            parsed_data = self.extract_grammar_result_gpt(data)
            
            if parsed_data is None:
                result[model_key][task_id] = {
                    "error": "failed to parse grammar"
                }
                continue

            result[model_key][task_id] = {
                "template": base_template,
                "helper_functions": parsed_data["helper_functions"],
                "basic_structure": parsed_data["basic_structure"],
                "inputs": parsed_data["inputs"],
                "contract_defs": parsed_data["contract_defs"],
                "constraints": data['grammar'][0].get("constraints")[0],
                "single_toggles": data.get("single_toggles")
            }

            
        return result
    
    def _parse_SFT_RL_format(self, data_list: List[Dict[str, Any]], model_key: str) -> Dict[str, Dict[str, Any]]:
        result = {}
        result[model_key] = {}
        base_template = ADT_BASE_TEMPLATE

        for data in data_list:
            task_id = data.get('name')
            parsed_data = self.extract_grammar_result_for_reward_sft_rl(data)
            
            if parsed_data is None:
                result[model_key][task_id] = {
                    "error": "failed to parse grammar"
                }
                continue

            result[model_key][task_id] = {
                "template": base_template,
                "helper_functions": parsed_data["helper_functions"],
                "basic_structure": parsed_data["basic_structure"],
                "inputs": parsed_data["inputs"],
                "contract_defs": parsed_data["contract_defs"],
                "constraints": data['grammar'][0].get("constraints")[0],
                "single_toggles": data.get("single_toggles")
            }

            
        return result
    
    def _parse_openllm_format(self, json_data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """parse open llm format"""
        result = {}
        
        # load json
        model_key = json_data["Setting"]["model_name"][0].split('/')[1]
        result[model_key] = {}
        base_template = ADT_BASE_TEMPLATE
        
        for data in json_data[model_key]:     
            parsed_data = self.extract_grammar_result(data)
            
            if parsed_data is None:
                result[model_key][data["task_id"]] = {
                    "error": "failed to parse grammar"
                }
                continue
 
            result[model_key][data["task_id"]] = {
                "template": base_template,
                "helper_functions": parsed_data["helper_functions"],
                "basic_structure": parsed_data["basic_structure"],
                "inputs": parsed_data["inputs"],
                "contract_defs": parsed_data["contract_defs"],
                "constraints": data['contracts_list'],
                "single_toggles": data.get("single_toggles")
            }

        return result
    
    def generate_contract_combinations(self, contract_defs: Dict[str, str]) -> List[Dict[str, bool]]:
        """generate all possible contract combinations excluding the all-true case (2^n - 2)"""
        contract_names = list(contract_defs.keys())
        n = len(contract_names)
        combinations = []
        
        # for i in range(1, 2**n): # all-true case is excluded
        for i in range(1, 2**n - 1):
            combination = {}
            for j in range(n):
                contract_name = contract_names[j]
                # if the j-th bit of i is 1, the contract is satisfied, otherwise it is violated
                combination[contract_name] = bool(i & (1 << j))
            combinations.append(combination)
        
        return combinations
    
class SMTTool:
    def __init__(self, solver_path: str = "z3", timeout: int = 30, num_solutions: int = 5, test_case_output_path: str = None):
        self.solver_path = solver_path
        self.timeout = timeout
        self.num_solutions = num_solutions
        self.test_case_output_path = test_case_output_path
    
    def check_solver_availability(self) -> bool:
        """check if smt solver is available"""
        try:
            result = subprocess.run(
                [self.solver_path, "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            return False


    ##############################################################
    # Apply schema to solutions by combination
    def apply_schema_to_solutions_by_combination(
        self,
        solutions: list[dict],
        constraints: dict[str, str],
        combination: dict[str, bool],
    ) -> None:

        rules = self.parse_constraint_rules(constraints)
        schema = self.build_post_schema_for_combination_from_constraints(rules, combination)

        for sol in solutions:
            tc = sol.get('test_case', {})
            for var, rule in schema.items():
                if var in tc and isinstance(tc[var], list):
                    if rule['type'] == 'tuple':
                        tc[var] = tuple(tc[var])    # convert empty list to empty tuple ()
                    elif rule['type'] == 'dict':
                        tc[var] = self._list_to_dict(tc[var])
            sol['test_case'] = tc

    def parse_constraint_rules(self, constraints: dict[str, str]) -> dict[str, dict]:
        """
        constraints:
        {'assert_0': 'assert isinstance(test_tup1, tuple), "invalid inputs',
        'assert_1': 'assert isinstance(test_tup2, tuple), "invalid inputs'}
        return:
        {'assert_0': {'var': 'test_tup1', 'type': 'tuple'},
        'assert_1': {'var': 'test_tup2', 'type': 'tuple'}}
        """
        rules: dict[str, dict] = {}
        for akey, text in constraints.items():
            if not isinstance(text, str):
                continue
            # tuple
            m = re.search(r"assert\s+isinstance\(\s*([A-Za-z_]\w*)\s*,\s*tuple\s*\)", text)
            if m:
                rules[akey] = {'var': m.group(1), 'type': 'tuple'}
                continue
            # dict
            m = re.search(r"assert\s+isinstance\(\s*([A-Za-z_]\w*)\s*,\s*dict\s*\)", text)
            if m:
                rules[akey] = {'var': m.group(1), 'type': 'dict'}
                continue
            # if needed, add more patterns here (e.g. set, list-of-pairs, etc.)
        return rules

    def build_post_schema_for_combination_from_constraints(
        self,
        constraint_rules: dict[str, dict],
        combination: dict[str, bool],
    ) -> dict[str, dict]:
        """
        combination: {'assert_0': True, 'assert_1': False, ...}
        return: {'var_name': {'type': 'tuple'|'dict'}}
        - False(violation) assert is not reflected (conversion is prohibited).
        - If tuple and dict are both entered for the same variable, dict is prioritized.
        """
        schema: dict[str, dict] = {}
        for akey, is_true in combination.items():
            if not is_true:
                continue
            info = constraint_rules.get(akey)
            if not info:
                continue
            var, typ = info['var'], info['type']
            if var not in schema or typ == 'dict':  # dict is more structured → priority
                schema[var] = {'type': typ}
        return schema


    def _list_to_dict(self, v: list):
        # [(k,v), ...]
        if all(isinstance(x, (list, tuple)) and len(x) == 2 for x in v):
            return {x[0]: x[1] for x in v}
        # [k1, v1, k2, v2, ...]
        if len(v) % 2 == 0:
            it = iter(v)
            return dict(zip(it, it))
        return v  # if conversion is not possible, keep the original
    ##############################################################


    def _z3_value_to_python(self, v):
        """ADT(Value) → python"""
        """If do not have value, update this function"""
        if v is None: return None
        d = v.decl().name(); ch = v.children()
        if d == "IntVal":   return ch[0].as_long()
        if d == "FloatVal": return float(Fraction(str(ch[0])))
        if d == "StrVal":   return ch[0].as_string()
        if d == "BoolVal":  return bool(is_true(ch[0]))
        if d == "Nil":      return []
        if d == "Cons":
            head_py = self._z3_value_to_python(ch[0])
            tail_py = self._z3_value_to_python(ch[1])
            return [head_py] + (tail_py if isinstance(tail_py, list) else [tail_py])
        return str(v)

    def _collect_input_bindings_from_model(self, m):
        """collect input bindings from model"""
        inputs = {}
        for decl in m.decls():
            if decl.arity() != 0:  # exclude function
                continue
            name = decl.name()
            try:
                val = m[decl]
            except Exception:
                val = m.eval(decl(), model_completion=True)

            sort_name = val.sort().name() if hasattr(val.sort(), "name") else str(val.sort())
            if sort_name == "Bool":
                continue

            top = val.decl().name()
            if top in {"IntVal","FloatVal","StrVal","BoolVal","Nil","Cons"}:
                inputs[name] = self._z3_value_to_python(val); continue

            if sort_name == "Int":
                inputs[name] = val.as_long();  continue
            if sort_name == "Real":
                inputs[name] = float(Fraction(str(val)));  continue
            if sort_name == "String":
                inputs[name] = val.as_string();  continue
        return inputs

    def _parse_model(self, solver_output):
        """parse model from solver output"""
        model = {}
        if hasattr(solver_output, 'decls'):
            for decl in solver_output.decls():
                name = decl.name(); arity = decl.arity()
                try:
                    if arity == 0:
                        model[name] = str(solver_output[decl])
                    else:
                        fi = solver_output.get_interp(decl)
                        model[name] = "<uninterpreted-func>" if fi is None else str(getattr(fi, "as_list", lambda: fi)())
                except Exception:
                    model[name] = "unknown"
            return model
        # string model
        if isinstance(solver_output, str):
            lines = solver_output.split('\n'); in_model = False
            for line in map(str.strip, lines):
                if line == "(get-model)": in_model = True; continue
                elif line.startswith("(") and line.endswith(")"): in_model = False; continue
                if in_model and line.startswith("(define-fun"):
                    try:
                        parts = line.split()
                        if len(parts) >= 5:
                            var_name = parts[1]; value = parts[-1].rstrip(')')
                            model[var_name] = value
                    except:
                        pass
        return model


    def run_smt_solver(self, smt_script: str, task_id: str) -> Tuple[bool, Optional[str], Optional[List[Dict[str, Any]]]]:
        
        try:
            # write smt script to temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.smt2', delete=False) as f:
                f.write(smt_script)
                temp_file = f.name
            
            # use z3 to find multiple solutions
            try:
                # Setting
                s = Solver()
                s.set(timeout=self.timeout*1000) # *1000 for ms
                assertions = parse_smt2_file(temp_file)
                s.add(assertions)
                
                # Find multiple solutions
                solutions = []
                seen_solutions = set()
                for i in range(self.num_solutions):
                    result = s.check()
                    if result.r != 1:  # unsat or unknown
                        break

                    m = s.model()

                    # 1) Parsing test case only (python value) + parsing entire model (optional)
                    test_case    = self._collect_input_bindings_from_model(m)   # ★ only input constants
                    parsed_model = self._parse_model(m)                         # (optional) string interpretation

                    # 2) Stable duplicate key (based on input only)  ★
                    key = json.dumps(test_case, sort_keys=True, ensure_ascii=False)
                  
                    if key not in seen_solutions:
                        solutions.append({
                            "test_case":  test_case,     # ★ actual input to use
                            #"model":      parsed_model,  # (optional) string interpretation
                            #"z3_model":   str(m),
                            "solution_id": len(solutions) + 1
                        })
                        seen_solutions.add(key)

                    # 3) Blocking constraints for finding next solution (only for input constants)  ★
                    if i < self.num_solutions - 1:
                        block_terms = []
                        for decl in m.decls():
                            if decl.arity() != 0:
                                continue  # exclude functions
                            try:
                                val = m[decl]  # constant interpretation
                            except Exception:
                                val = m.eval(decl(), model_completion=True)

                            # Bool constants (C0/C1/C2) are not inputs, so exclude
                            sort_name = val.sort().name() if hasattr(val.sort(), "name") else str(val.sort())
                            if sort_name == "Bool":
                                continue

                            # Only include ADT(Value) or primitive sorts (Int/Real/String) in blocking
                            top = val.decl().name()
                            if top in {"IntVal", "FloatVal", "StrVal", "BoolVal", "Nil", "Cons"} or \
                            sort_name in {"Int", "Real", "String"}:
                                block_terms.append(decl() != val)  # Not(decl()==val)

                        if block_terms:
                            # To exclude exactly "current input assignment", we need to add them all at once with Or  ★
                            s.add(Or(block_terms))
                        else:
                            # If no inputs are seen, avoid infinite loop
                            break

                
                if solutions:
                    return True, f"Found {len(solutions)} solutions", solutions
                else:
                    return False, "unsat", None
                    
            except Exception as e:
                print("="*50)
                print(f"task_id: {task_id}")
                print("This means that the grammar is not correct")
                print(f"Z3 parsing error: {e}, fallback to subprocess")
                return "Z3 parsing error", None, None
            
        except subprocess.TimeoutExpired:
            return False, "Solver timeout", None
        except Exception as e:
            return str(e)

    def run_smt_solver_with_hard_timeout(self, smt_script: str, task_id: str, hard_timeout_sec: int) -> Tuple[bool, Optional[str], Optional[List[Dict[str, Any]]]]:
        """External hard timeout wrapper. If exceeded, mark as failure for this combination."""
        def _target(q: multiprocessing.Queue):
            try:
                res = self.run_smt_solver(smt_script, task_id)
                q.put(("ok", res))
            except Exception as e:
                q.put(("err", f"{type(e).__name__}: {e}"))

        q: multiprocessing.Queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=_target, args=(q,))
        p.start()
        p.join(hard_timeout_sec)
        if p.is_alive():
            p.terminate()
            p.join()
            return False, "HardTimeout", None
        if not q.empty():
            tag, payload = q.get()
            if tag == "ok":
                try:
                    # payload is a tuple (bool_or_str, msg, sols)
                    return payload[0], payload[1], payload[2]
                except Exception:
                    return False, "MalformedResult", None
            else:
                return False, payload, None
        return False, "NoResult", None

    def _parse_model(self, solver_output) -> Dict[str, Any]:
        """parse model from solver output - support both z3 model object and string"""
        model = {}

        # if solver_output is z3 model object
        if hasattr(solver_output, 'decls'):
            for decl in solver_output.decls():
                name = decl.name()
                arity = decl.arity()
                try:
                    if arity == 0:
                        # only constant is evaluated
                        # value = solver_output.eval(decl())  # also possible
                        value = solver_output[decl]            # preferred: direct lookup
                        model[name] = str(value)
                    else:
                        # do not call function, only keep interpretation
                        fi = solver_output.get_interp(decl)     # FuncInterpRef or None
                        if fi is None:
                            model[name] = "<uninterpreted-func>"
                        else:
                            try:
                                model[name] = str(fi.as_list()) # [(args)->val, ..., else->val]
                            except Exception:
                                model[name] = str(fi)
                except Exception:
                    model[name] = "unknown"
            return model

        # string model
        if isinstance(solver_output, str):
            lines = solver_output.split('\n')
            in_model = False

            for line in lines:
                line = line.strip()
                if line == "(get-model)":
                    in_model = True
                    continue
                elif line.startswith("(") and line.endswith(")"):
                    in_model = False
                    continue

                if in_model and line.startswith("(define-fun"):
                    try:
                        parts = line.split()
                        if len(parts) >= 5:
                            var_name = parts[1]
                            value = parts[-1].rstrip(')')
                            model[var_name] = value
                    except:
                        continue

        return model

    
    def data_loader(self, mode: str, task_id: str) -> Dict[str, Any]:
        if mode == "humaneval":
            jsonl_path = "/home/imsuhan22/Soohan_file/2.contracts_testcase_generation/SHERLOCK/data/evalplus-0.1.1/HumanEvalPlus.jsonl"
        elif mode == "mbpp":
            jsonl_path = "/home/imsuhan22/Soohan_file/2.contracts_testcase_generation/SHERLOCK/data/mbppplus-0.2.0/MbppPlus.jsonl"
        else:
            raise ValueError(f"Unsupported mode: {mode}")
        
        with open(jsonl_path, "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
   
        if task_id:
            for item in data:
                if item['task_id'] == task_id:
                    return item['contract']
            return None
        else:
            return data
    
    def initial_save_after_quality_train_data(self, output_dir: str, model_name: str) -> None:
        """Initialize after quality train data file by overwriting if exists"""
        if os.path.isdir(output_dir) or not output_dir.endswith('.jsonl'):
            output_dir = os.path.join(output_dir, f'{model_name}_train_data.jsonl')
        
        os.makedirs(os.path.dirname(output_dir), exist_ok=True)
        with open(output_dir, 'w', encoding='utf-8') as f:
            pass
    
    def save_after_quality_train_data(self, grammar_file: str, task_id: str, after_quality_string: str, output_dir: str, model_name: str) -> None:
        """Append SMT script data to JSONL file"""
        if os.path.isdir(output_dir) or not output_dir.endswith('.jsonl'):
            output_dir = os.path.join(output_dir, f'{model_name}_train_data.jsonl')
        
        os.makedirs(os.path.dirname(output_dir), exist_ok=True)
        
        with open(grammar_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    item = json.loads(line)
                    if item.get('name') == task_id:
                        item['grammar'][0]['production'] = after_quality_string
                        
                        with open(output_dir, 'a', encoding='utf-8') as output_f:
                            
                            json.dump(item, output_f, ensure_ascii=False)
                            output_f.write('\n')
                        break
    
    
    def initial_save_smt_script(self, output_file: str, model_name: str) -> None:
        """Initialize SMT script file by overwriting if exists"""
        # if output_file is directory, add smt_script.jsonl file name
        if os.path.isdir(output_file) or not output_file.endswith('.jsonl'):
            output_file = os.path.join(output_file, f'{model_name}-smt_script.jsonl')
        
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            pass
    
    def save_smt_script(self, save_smt_script_data_per_task: Dict[str, Any], output_file: str, model_name: str) -> None:
        """Append SMT script data to JSONL file"""
        # if output_file is directory, add smt_script.jsonl file name
        if os.path.isdir(output_file) or not output_file.endswith('.jsonl'):
            output_file = os.path.join(output_file, f'{model_name}-smt_script.jsonl')
        
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'a', encoding='utf-8') as f:
            json.dump(save_smt_script_data_per_task, f, ensure_ascii=False)
            f.write('\n')
    
    def generate_test_cases(self, 
                            grammar_data: Dict[str, Any], base_template: str, 
                            task_id: str, model_name: str, 
                            failed_smt_solver_tasks: List[str] = None, grammar_file: str = None, 
                            test_case_output_path: str = None, verbose: bool = True,
                            hard_timeout_sec: Optional[int] = None) -> List[Dict[str, Any]]:
        
        
        test_cases = {}
        is_satisfiable_list = []
        is_satisfiable = False  # default when no combinations are generated
        combinations = self._generate_contract_combinations(grammar_data["constraints"])
        save_smt_script_data_per_task = {}
        save_smt_script_data_per_task[task_id] = {'base_smt_script': [], 'combination': []}  
        all_contracts_true_failed = False
        all_contract_true_not_only = False
        train_data_save_flag = False

        for idx, combination in enumerate(combinations):
            # Generate SMT script
            smt_script, base_smt_script, combination_str, after_quality_train_sample = self._format_smt_script(base_template, grammar_data, combination, model_name)
            if len(save_smt_script_data_per_task[task_id]['base_smt_script']) == 0:
                save_smt_script_data_per_task[task_id]['base_smt_script'] = base_smt_script
            # Run solver with multiple solutions
            try: 
                ht = hard_timeout_sec if hard_timeout_sec is not None else max(1, self.timeout + 5)
                is_satisfiable, solver_output, solutions = self.run_smt_solver_with_hard_timeout(smt_script, task_id, ht)
                
                # ** Update-1 ** if you want to check z3
                #is_satisfiable, solver_output, solutions = self.run_smt_solver(smt_script, task_id)
                
                if is_satisfiable == "Z3 parsing error":
                    continue

                is_satisfiable_list.append(is_satisfiable)
                if is_satisfiable == True:
                    self.apply_schema_to_solutions_by_combination(solutions=solutions,constraints=grammar_data["constraints"],combination=combination)
                    #print(grammar_data["constraints"])
                    #print(combination)
                    #print(solutions)
                    save_smt_script_data_per_task[task_id]['combination'].append({combination_str: combination})
                    
                    # save after quality train data
                    if model_name == "o4-mini" and train_data_save_flag == False:
                        after_quality_string = json.dumps(after_quality_train_sample, ensure_ascii=False, indent=2)
                        after_quality_string_json = f"\n```json\n{after_quality_string}\n```\n"
                        self.save_after_quality_train_data(grammar_file, task_id, after_quality_string_json, test_case_output_path, model_name)
                        train_data_save_flag = True
                
                if all(combination.values()) and is_satisfiable == False:
                    all_contracts_true_failed = True
                
                if ((not all(combination.values())) or len(combination) == 1) and is_satisfiable == True:
                    all_contract_true_not_only = True
                
                if verbose:
                    print("="*50)
                    print(f"task_id: {task_id}")
                    if "humaneval" in grammar_file:
                      print("contract list: ", self.data_loader("humaneval", task_id))
                    elif "mbpp" in grammar_file:
                      print("contract list: ", self.data_loader("mbpp", task_id))
                    else:
                        raise ValueError(f"Unsupported dataset: {grammar_file}")
                    print(combination)
                    print("is_satisfiable: ", is_satisfiable)

            except Exception as e: 
                if failed_smt_solver_tasks is not None:
                    if task_id not in failed_smt_solver_tasks:
                        failed_smt_solver_tasks.append(task_id)
                continue
            
            #print("solver_output: ", solver_output)
            if verbose:
                print("solutions: ", solutions)
            # Combination name generation
            satisfied_contracts = [name for name, satisfied in combination.items() if satisfied]
            violated_contracts = [name for name, satisfied in combination.items() if not satisfied]
            combination_name = f"satisfied_{';'.join(satisfied_contracts)}, violated_{';'.join(violated_contracts)}"
            
            # Generate test case with multiple solutions
            test_cases[combination_name] = {
                "combination": combination,
                "smt_script": smt_script,
                "solver_result": solver_output,
                "is_satisfiable": is_satisfiable,
                "solutions": solutions if solutions else [],
                "solution_count": len(solutions) if solutions else 0,
                "metadata": {
                    "satisfied_contracts": satisfied_contracts,
                    "violated_contracts": violated_contracts,
                    "total_contracts": len(combination)
                }
            }

        if model_name != "reward":
            self.save_smt_script(save_smt_script_data_per_task, self.test_case_output_path, model_name)
        return test_cases, all_contracts_true_failed, failed_smt_solver_tasks, all_contract_true_not_only, is_satisfiable, is_satisfiable_list
    
    def _generate_contract_combinations(self, contract_defs: Dict[str, str]) -> List[Dict[str, bool]]:
        """Generate all possible contract combinations excluding empty and all-true (2^n - 2).
        Special case: if there is only one contract, generate the single 'violated-only' combination.
        """
        # ** Update-2 ** Skipe null contracts
        # Skip contracts whose value indicates disabled (0 or "0")
        def _is_disabled(v):
            if v is None:
                return True
            return False

        contract_names = [k for k, v in contract_defs.items() if not _is_disabled(v)]
        n = len(contract_names)
        if n == 0:
            return []
        
        # Special-case: for a single contract, return only the violated case
        if n == 1:
            return [{contract_names[0]: False}]

        combinations = []
        
        # Generate all non-empty subsets (0 to 2^n-1)
        #for i in range(0, 2**n):  # Start from 0
        # Generate all subsets excluding empty(0) and all-true(2^n-1)
        for i in range(1, 2**n - 1):
            combination = {}
            for j in range(n):
                contract_name = contract_names[j]
                # If the j-th bit of i is 1, the contract is satisfied, otherwise it is violated
                combination[contract_name] = bool(i & (1 << j))
            combinations.append(combination)
        
        return combinations
    
    def _format_smt_script(self, base_template: str, grammar_data: Dict[str, Any], combination: Dict[str, bool], model_name: str) -> str:
        """SMT Script Generation"""
        script = str(base_template)
        helper_functions = grammar_data["helper_functions"]
        inputs = grammar_data["inputs"]
        basic_structure = grammar_data["basic_structure"]
        
        if isinstance(grammar_data["contract_defs"], list):
            contract_defs_str = "\n".join(grammar_data["contract_defs"])
        elif isinstance(grammar_data["contract_defs"], str):
            contract_defs_str = grammar_data["contract_defs"]
        elif isinstance(grammar_data["contract_defs"], dict):
            contract_defs_str = "\n".join(grammar_data["contract_defs"].values())
        else:
            raise ValueError(f"Unknown contract_defs type: {type(grammar_data['contract_defs'])}")
            
        if model_name == "o4-mini":
            for i in [('re-union', 're.union'), ('re-concat', 're.++'), 
                      ('re-star', 're.*'),
                      (' 1e-5', ' (/ 1 100000)'), (' 1e-6', ' (/ 1 1000000)')]:
                helper_functions = helper_functions.replace(i[0], i[1])
                basic_structure = basic_structure.replace(i[0], i[1])
                inputs = inputs.replace(i[0], i[1])
                contract_defs_str = contract_defs_str.replace(i[0], i[1])
                
        after_quality_train_sample = {
            "helper_functions": helper_functions,
            "inputs": inputs,
            "basic_structure": basic_structure,
            "contract_defs": contract_defs_str
        }
        
        # Insert contract combinations
        import re
        ordered_keys = sorted(combination.keys(), key=lambda k: int(re.search(r'\d+', k).group()))
        combination_assertions = []
        for k in ordered_keys:
            satisfied = combination[k]
            m = re.match(r'assert_(\d+)$', k)
            if not m:
                raise ValueError(f"Unknown contract key: {k}")
            contract_id = f"C{m.group(1)}"   # assert_0 -> C0, assert_1 -> C1, ...

            combination_assertions.append(f"(assert {contract_id})" if satisfied else f"(assert (not {contract_id}))")
        
        combination_str = "\n".join(combination_assertions)
            
        # Replace place holder with llm model output
        for key, value in [("<<HELPER_FUNCTIONS>>", helper_functions), 
                           ("<<INPUT>>", inputs), 
                           ("<<BASIC_STRUCTURE>>", basic_structure), 
                           ("<<CONTRACT_DEFS>>", contract_defs_str), 
                           ("<<COMBINATION>>", combination_str)]:        
            
            if key == "<<COMBINATION>>":
                base_smt_script = script
            
            if not isinstance(value, list):
                script = script.replace(key, str(value))    
            else:
                script = script.replace(key, "\n".join(str(v) for v in value))
        
        for k in ["; === ADD HELPER FUNCTIONS HERE ===", "; === Inputs ===", "; === BASIC STRUCTURE ===", "; === Contract predicates ==="]:
            if script.count(k) > 1:
                script = script.replace(k, "", 1)
        
        return script, base_template, combination_str, after_quality_train_sample
    
    def filter_satisfiable_cases(self, test_cases: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """filter satisfiable test cases"""
        return [tc for tc in test_cases if tc["is_satisfiable"]]
    
    def filter_violation_cases(self, test_cases: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """filter violation test cases"""
        violation_cases = []
        
        for tc in test_cases:
            # if any False(violation) exists, it is violation case
            if any(not satisfied for satisfied in tc["combination"].values()):
                violation_cases.append(tc)
        
        return violation_cases
    
    def export_test_cases(self, test_cases: Dict[str, Any], 
                         output_file: str, model_name: str, failed_smt_solver_tasks: List[str] = None, all_contracts_true_failed_tasks: List[str] = None, all_contract_true_only_tasks: List[str] = None, format: str = "json") -> None:
        """export test cases to file"""
        if format.lower() == "json":
            self._export_json(test_cases, output_file, model_name)
        elif format.lower() == "txt":
            self._export_txt(test_cases, output_file, model_name, failed_smt_solver_tasks, all_contracts_true_failed_tasks, all_contract_true_only_tasks)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _export_json(self, test_cases: Dict[str, Any], output_file: str, model_name: str) -> None:
        """JSON format export - improved version"""
        export_data = {
            "metadata": {
                "model_name": model_name,
                "total_test_cases": len(test_cases),
                "generation_timestamp": str(datetime.datetime.now()),
                "solver_config": {
                    "solver_path": self.solver_path,
                    "timeout": self.timeout,
                    "num_solutions": self.num_solutions
                }
            },
            "test_cases": {}
        }
        
        for task_id, task_cases in test_cases[model_name].items():
            export_data["test_cases"][task_id] = {}
            for combination_name, tc in task_cases.items():
                tc_data = {
                    "combination": tc["combination"],
                    "is_satisfiable": tc["is_satisfiable"],
                    "solution_count": tc["solution_count"],
                    "solutions": tc["solutions"],
                    "metadata": tc["metadata"],
                    "smt_script": tc["smt_script"]
                }
                export_data["test_cases"][task_id][combination_name] = tc_data
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
    
    def _export_txt(self, test_cases: Dict[str, Any], output_file: str, model_name: str, failed_smt_solver_tasks: List[str] = None, all_contracts_true_failed_tasks: List[str] = None, all_contract_true_only_tasks: List[str] = None) -> None:
        """txt format export - improved version"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"=== SMT Test Cases Report ===\n")
            f.write(f"Generated: {datetime.datetime.now()}\n")
            f.write(f"Model: {model_name}\n")
            f.write(f"Solver: {self.solver_path}\n")
            f.write(f"Solutions per case: {self.num_solutions}\n")
            f.write(f"tasks failed when smt solver failed: {failed_smt_solver_tasks}\n")
            f.write(f"tasks failed when all contracts true: {all_contracts_true_failed_tasks}\n")
            f.write(f"tasks failed when all contracts true only: {all_contract_true_only_tasks}\n")
            f.write("=" * 50 + "\n\n")
            
            for task_id, task_cases in test_cases[model_name].items():
                f.write(f"=== Task: {task_id} ===\n")
                for i, (combination_name, tc) in enumerate(task_cases.items(), 1):
                    f.write(f"  Test Case {i}: {combination_name}\n")
                    f.write(f"  Combination: {tc['combination']}\n")
                    f.write(f"  Satisfiable: {tc['is_satisfiable']}\n")
                    f.write(f"  Solution Count: {tc['solution_count']}\n")
                    f.write(f"  Metadata: {tc['metadata']}\n")
                    
                    if tc["solutions"]:
                        f.write(f"  Solutions:\n")
                        for j, solution in enumerate(tc["solutions"], 1):
                            f.write(f"    Solution {j}:\n")
                            f.write(f"      test_case: {solution['test_case']}\n")
                    
                    f.write(f"  SMT Script:\n{tc['smt_script']}\n")
                    f.write("-" * 30 + "\n")
                f.write("=" * 50 + "\n\n")

class GrammarSMTTool:
    def __init__(self, solver_path: str = "z3", timeout: int = 30, num_solutions: int = 3, test_case_output_path: str = None):
        self.grammar_tool = GrammarTool()
        self.smt_tool = SMTTool(solver_path, timeout, num_solutions, test_case_output_path)
    
    def save_json(self, data: Dict[str, Any], output_file: str) -> None:
        """save data to json file"""
        os.makedirs(os.path.dirname(f"{output_file}/"), exist_ok=True)
        with open(f"{output_file}/on_going_smt_result.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    
    def process_grammar_file(self, grammar_file: str, output_dir: str = "output", model_name: str = None, 
                             test_case_output_path: str = None, test_case_output_path_model: str = None) -> bool:
        """This is the main function to process the grammar file"""
 
        try:
            print(f"Processing Grammar File: {grammar_file}")
            
            total_start_time = time.time()
            
            # adjust task id
            adjusted_grammar_results = {}
            if "humaneval" in grammar_file:
                dataset_key = "humaneval"
            else:
                dataset_key = "mbpp"
            
            if model_name == "o4-mini":
                adjusted_file=os.path.join(os.path.dirname(grammar_file), f"{dataset_key}_adjust.jsonl")
                if os.path.exists(adjusted_file):
                    with open(adjusted_file, "r", encoding='utf-8') as m:
                        for odd_line in [line for line in m if m != ""]:
                            odd_line = odd_line.strip()
                            adjusted_grammar_results[json.loads(odd_line)["name"]] = json.loads(odd_line)
                else:
                    print(f"✗ No adjusted file found: {adjusted_file}")
        
            # Load Grammar JSON file
            if grammar_file.endswith(".jsonl"):
                grammar_results = []
                with open(grammar_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            if json.loads(line)["name"] in adjusted_grammar_results.keys():
                                grammar_results.append(adjusted_grammar_results[json.loads(line)["name"]])
                            else:
                                grammar_results.append(json.loads(line))
                        
            else:
                with open(grammar_file, 'r', encoding='utf-8') as f:
                    grammar_results = json.load(f)

            # Parse JSON - GPT model and Open LLM model are supported
            grammar_results = self.grammar_tool.parse_grammar_json(grammar_results, model_name)
            if grammar_results == {}:
                print(f"✗ No grammar results found in {grammar_file}")
                return False
            
            print(f"✓ Parsed Grammar JSON")
            os.makedirs(f"{os.path.dirname(output_dir)}", exist_ok=True)
            
            # Save parsed data as JSON
            with open(f"{output_dir}", "w") as f:
                json.dump(grammar_results, f, indent=2)
            
            # Save parsed data as CSV (similar to inference_parsing.py)
            csv_file_name = output_dir.split("/")[-1].split(".")[0]
            csv_output = f"{os.path.dirname(output_dir)}/{csv_file_name}.csv"
            self._save_parsed_summary_to_csv(grammar_results, csv_output, grammar_file)
            print(f"✓ Parsed summary saved to CSV: {csv_output}")
            
            # Check SMT solver
            if not self.smt_tool.check_solver_availability():
                print(f"✗ SMT solver not found: {self.smt_tool.solver_path}")
                print("Please install Z3 or specify the correct path")
                return False
            print(f"✓ SMT solver check completed: {self.smt_tool.solver_path}")
            
            # Generate base template
            base_template = ADT_BASE_TEMPLATE
            
            # Generate test cases
            print("Generating test cases...")
            self.smt_tool.initial_save_smt_script(test_case_output_path, model_name)
            
            if model_name == "o4-mini":
                self.smt_tool.initial_save_after_quality_train_data(os.path.dirname(test_case_output_path), model_name)
            
            all_test_cases = {model_name:{}}
            all_contract_true_only_tasks = {}
            all_contracts_true_failed_tasks = []  # failed tasks
            failed_smt_solver_tasks = []
            
            task_processing_start_time = time.time()

            # Extract inputs from the first model's first sample
            for _, samples in grammar_results.items():
                for task_id, sample in samples.items():
                    
                    # # Debugging #########################################################
                    # if task_id != "HumanEval/10":
                    #   - processed tasks X: ['HumanEval/10', 'HumanEval/12', 'HumanEval/21', 'HumanEval/27', 'HumanEval/30', 'HumanEval/34', 'HumanEval/54', 'HumanEval/58', 'HumanEval/64', 'HumanEval/77', 'HumanEval/101', 'HumanEval/134', 'HumanEval/140', 'HumanEval/151']
                    #     continue
                    # #####################################################################
                    
                    try:
                        if "error" in sample.keys():
                            print(f"Error in {task_id}")
                            failed_smt_solver_tasks.append(task_id)
                            continue
                        
                        test_cases, all_contracts_true_failed, failed_smt_solver_tasks, all_contract_true_not_only, is_satisfiable, is_satisfiable_list = self.smt_tool.generate_test_cases(sample, base_template, task_id, model_name, failed_smt_solver_tasks, grammar_file, os.path.dirname(test_case_output_path), verbose=True)
                        all_test_cases[model_name][task_id] = test_cases
                        
                        # if all contracts are true, it is failed task
                        if all_contracts_true_failed:
                            all_contracts_true_failed_tasks.append(task_id)
                        
                        # if all contracts are true only, it is failed task
                        if all_contract_true_not_only and is_satisfiable:
                            all_contract_true_only_tasks[task_id] = all_contract_true_not_only
                        else:
                            # Only set to False if not already set to True
                            if task_id not in all_contract_true_only_tasks:
                                all_contract_true_only_tasks[task_id] = False
                        
                        self.save_json(all_test_cases, test_case_output_path)
                    except Exception as e:
                        print(f"Error in {task_id}")
                        print(e)
            
            task_processing_end_time = time.time()
            task_processing_duration = task_processing_end_time - task_processing_start_time
            
            # calculate the number of tasks that are processed successfully (not empty dict)
            processed_tasks=[]
   
            for task_number in all_test_cases[model_name]:
                for combination_name in all_test_cases[model_name][task_number]:
                    if all_test_cases[model_name][task_number][combination_name]['is_satisfiable']:
                        processed_tasks.append(task_number)
                        break
            
            print(f"✓ {len(processed_tasks)} tasks processed successfully")

            # Create output directory
            os.makedirs(test_case_output_path, exist_ok=True)
            
            # export results
            json_output = os.path.join(test_case_output_path, f"{test_case_output_path_model}-smt_result.json")
            txt_output = os.path.join(test_case_output_path, f"{test_case_output_path_model}-smt_result.txt")
            time_txt_output = os.path.join(test_case_output_path, f"{test_case_output_path_model}-smt_result_time.txt")
            
            self.smt_tool.export_test_cases(all_test_cases, json_output, model_name,"json")
            self.smt_tool.export_test_cases(all_test_cases, txt_output, model_name, failed_smt_solver_tasks, all_contracts_true_failed_tasks, all_contract_true_only_tasks, "txt")
            
            print(f"✓ results saved successfully:")
            print(f"  - JSON: {json_output}")
            print(f"  - TXT: {txt_output}")
            

            total_end_time = time.time()
            total_duration = total_end_time - total_start_time
            
            # print statistics and log to CSV
            total_cases = sum(len(task_cases) for task_cases in all_test_cases[model_name].values())
            total_cases_generated = sum(1 for task_cases in all_test_cases[model_name].values() for tc in task_cases.values() if tc["is_satisfiable"])
            total_solutions = sum(sum(tc.get('solution_count', 0) for tc in task_cases.values()) for task_cases in all_test_cases[model_name].values()
            )
            
            tasks_with_satisfiable = sum(1 for task_cases in all_test_cases[model_name].values() if any(tc["is_satisfiable"] for tc in task_cases.values())) 
            
            print(f"\n📊 this is the statistics of the test cases:")
            print(f"  - processed tasks O: {processed_tasks}")
            print(f"  - processed tasks X: {[task_id for task_id in all_test_cases[model_name].keys() if task_id not in processed_tasks]}")
            print(f"  - tasks with satisfiable: {tasks_with_satisfiable}")
            print("="*50)
            print(f"  - total test cases processed (all): {total_cases}") # this is the number of contract combinations 
            print(f"  - total test cases proccessed (generated): {total_cases_generated}") # this is the number of test cases generated by smt solver in contract combinations
            print(f"  - total solutions: {total_solutions}")
            print(f"  - average solutions per case: {self.smt_tool.num_solutions}")
            print("="*50)
            print(f"  - tasks failed when smt solver failed: {failed_smt_solver_tasks}")
            print(f"  - tasks failed when all contracts true: {all_contracts_true_failed_tasks}")
            print(f"  - tasks failed when all contracts true only: {[task_id for task_id, value in all_contract_true_only_tasks.items() if value != True]}")
            print("="*50)
            print(f"  - task processing time: {task_processing_duration/60:.2f} minutes")
            print("="*50)
            #print(f"  - total processing time: {total_duration:.2f} seconds")
            
            self._save_timing_info_to_txt(time_txt_output, task_processing_duration, total_duration, len(processed_tasks), total_cases, total_solutions)
            
            # add all_contracts_true_failed_tasks information to CSV logging
            self._log_to_csv(test_case_output_path, model_name, model_name, 
                             total_cases, total_solutions, processed_tasks, 
                             grammar_file, tasks_with_satisfiable, all_contracts_true_failed_tasks)
            
            return True
            
        except Exception as e:
            print(f"✗ Error: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _log_to_csv(self, output_dir: str, base_name: str, model_name: str, 
                    total_cases: int, total_solutions: int, total_tasks: int, 
                    grammar_file: str, tasks_with_satisfiable: int = 0, 
                    all_contracts_true_failed_tasks: List[str] = None) -> None:
        """log parsing results to CSV file"""
        csv_output = os.path.join(output_dir, f"{base_name}-smt_result_log.csv")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if all_contracts_true_failed_tasks is None:
            all_contracts_true_failed_tasks = []
        
        # determine whether to write CSV header
        write_header = not os.path.exists(csv_output) or os.stat(csv_output).st_size == 0
        
        with open(csv_output, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            if write_header:
                writer.writerow([
                    "timestamp",
                    "model_name",
                    "grammar_file",
                    "total_tasks", # this is the number of tasks that are processed successfully
                    "total_test_cases", # this is the number of test cases that are generated by smt solver
                    "tasks_with_satisfiable", # this is the number of tasks that have at least one satisfiable test case
                    "total_solutions", # this is the number of solutions that are generated by smt solver
                    "avg_solutions_per_case", # this is the average number of solutions per test case
                    "solver_path", # this is the path of the smt solver
                    "timeout", # this is the timeout of the smt solver
                    "num_solutions_per_case", # this is the number of solutions per test case
                    "all_contracts_true_failed_count", # this is the number of tasks that failed when all contracts are true
                    "all_contracts_true_failed_tasks", # this is the list of task_ids that failed when all contracts are true
                ])
            
            writer.writerow([
                timestamp,
                model_name,
                os.path.basename(grammar_file),
                total_tasks,
                total_cases,
                tasks_with_satisfiable,
                total_solutions,
                round(total_solutions / total_cases, 2) if total_cases > 0 else 0,
                self.smt_tool.solver_path,
                self.smt_tool.timeout,
                self.smt_tool.num_solutions,
                len(all_contracts_true_failed_tasks),
                ",".join(all_contracts_true_failed_tasks) if all_contracts_true_failed_tasks else ""
            ])
        
        print(f"✓ CSV log saved: {csv_output}")

    def _save_parsed_results_to_csv(self, grammar_results: Dict[str, Any], csv_output: str) -> None:
        """save parsed grammar results to CSV"""
        with open(csv_output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # write CSV header
            writer.writerow([
                "model_name",
                "task_id", 
                "helper_functions_count",
                "basic_structure_length",
                "inputs_count",
                "contract_defs_count",
                "single_toggles"
            ])
            
            # write data
            for model_name, samples in grammar_results.items():
                for task_id, sample in samples.items():
                    writer.writerow([
                        model_name,
                        task_id,
                        len(sample.get("helper_functions", [])),
                        len(sample.get("basic_structure", "")),
                        len(sample.get("inputs", [])),
                        len(sample.get("contract_defs", {})),
                        str(sample.get("single_toggles", ""))
                    ])

    def _save_parsed_summary_to_csv(self, grammar_results: Dict[str, Any], csv_output: str, grammar_file: str) -> None:
        """save parsed grammar results to CSV in the same format as inference_parsing.py"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # determine whether to write CSV header
        write_header = not os.path.exists(csv_output) or os.stat(csv_output).st_size == 0
        
        with open(csv_output, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            if write_header:
                writer.writerow([
                    "timestamp",
                    "model_name",
                    "success_len",
                    "failure_len",
                    "success_list",
                    "failure_list",
                    "complete_section_tasks",
                    "incomplete_section_tasks"
                ])
            
            # calculate statistics for each model
            for model_name, samples in grammar_results.items():
                success_list = []
                failure_list = []
                
                for task_id, sample in samples.items():
                    if "error" in sample:
                        failure_list.append(task_id)
                    else:
                        success_list.append(task_id)
                success_len = len(success_list)
                failure_len = len(failure_list)
                
                # calculate complete_section_tasks (number of tasks that have all fields)
                complete_section_tasks = 0
                for task_id, sample in samples.items():
                    if (sample.get("helper_functions") and 
                        sample.get("basic_structure") and 
                        sample.get("inputs") and 
                        sample.get("contract_defs")):
                        complete_section_tasks += 1

                incomplete_section_tasks = success_len - complete_section_tasks
                
                writer.writerow([
                    timestamp,
                    model_name,
                    success_len,
                    failure_len,
                    ",".join(success_list),
                    ",".join(failure_list),
                    complete_section_tasks,
                    incomplete_section_tasks
                ])

    def _save_timing_info_to_txt(self, txt_output: str, task_processing_time: float, total_time: float, 
                                processed_tasks_count: int, total_cases: int, total_solutions: int) -> None:
        try:
            with open(txt_output, 'w', encoding='utf-8') as f:
                f.write("\n" + "="*60 + "\n")
                f.write("TIMING INFORMATION\n")
                f.write("="*60 + "\n")
                f.write(f"Task Processing Time: {task_processing_time:.2f} seconds\n")
                f.write(f"Total Processing Time: {total_time:.2f} seconds\n")
                f.write(f"Processed Tasks Count: {processed_tasks_count}\n")
                f.write(f"Total Test Cases: {total_cases}\n")
                f.write(f"Total Solutions: {total_solutions}\n")
                f.write(f"Average Time per Task: {task_processing_time/processed_tasks_count:.2f} seconds\n" if processed_tasks_count > 0 else "Average Time per Task: N/A\n")
                f.write(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*60 + "\n")
        except Exception as e:
            pdb.set_trace()


def main():
    parser = argparse.ArgumentParser(description="Parse Grammar JSON and generate SMT test cases")
    parser.add_argument("-m", "--model", help="Model name")
    parser.add_argument("--grammar_file", help="Grammar JSON file path")
    parser.add_argument("-o", "--output_path", help="Output directory (default: output)")
    parser.add_argument("-s", "--solver", default="z3", help="SMT solver path (default: z3)")
    parser.add_argument("-t", "--timeout", type=int, default=30, help="Solver timeout (seconds, default: 30)")
    parser.add_argument("-n", "--num_solutions", type=int, default=3, help="Number of solutions per test case (default: 3)")
    parser.add_argument("-e", "--test_case_output_path", help="Test case output directory")
    parser.add_argument("--test_case_output_path_model", help="Test case output directory model")
    args = parser.parse_args()
    
    if not os.path.exists(args.grammar_file):
        print(f"❌ No file: {args.grammar_file}")
        return 1
    
    tool = GrammarSMTTool(solver_path=args.solver, timeout=args.timeout, num_solutions=args.num_solutions, test_case_output_path=args.test_case_output_path)
    success = tool.process_grammar_file(args.grammar_file, args.output_path, args.model, args.test_case_output_path, args.test_case_output_path_model)
    return 0 if success else 1

if __name__ == "__main__":
    main()