import json
import argparse
import os
import re
import pandas as pd
from datetime import datetime
import pdb
import csv
import ast
import codecs
import itertools

from data_load import load_section

SECTION_NAMES = load_section()

def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_type", type=str)
    parser.add_argument("--model_name", type=str)
    parser.add_argument("--test_case_type", type=str)
    args = parser.parse_args()  # for notebook/debugging
    return args

def generate_contract_combinations(contracts_list):
    """
    {'assert_0': '...', 'assert_1': '...', 'assert_2': '...'}
    -> {'assert_0': '...', 'assert_1': '...', 'assert_2': '...', 
        'assert_0,assert_1': '...', 'assert_0,assert_2': '...', 
        'assert_1,assert_2': '...', 'assert_0,assert_1,assert_2': '...'}
    """
    contract_list_total = contracts_list.copy()
    original_keys = sorted(contracts_list.keys())
    
    for r in range(2, len(original_keys) + 1):
        for combo in itertools.combinations(original_keys, r):
            combo_key = ','.join(combo)
            contract_list_total[combo_key] = combo_key
    
    return contract_list_total

def all_root(dataset_type, model_name, test_case_type):
    pwd = os.getcwd()
    
    if test_case_type == "contracts":
        tag = "cont"
    else:
        tag = "func"
    
    if "ours" in model_name:
        if 'deepseek' in model_name:
            model_name_tag = "DeepSeek-R1-Distill-Qwen-14B"
        elif 'mistral' in model_name:
            model_name_tag = "Mistral-Nemo-Base-2407"
    
    if model_name == "gpt-4o-mini" or model_name == "o4-mini":
        data_load_root = f'../../code/output_gpt/original/{model_name}/{test_case_type}/{dataset_type}_{model_name}_sft.jsonl'
        output_dir = f'../../code/output_gpt/{dataset_type}/parsing_data/{test_case_type}'
    elif "ours_sft" in model_name or "ours_rl" in model_name:
        data_load_root = f'../../code/output_our/{dataset_type}/inference/{test_case_type}/{model_name_tag}/{dataset_type}_{tag}_sft_pass@1.jsonl'
        output_dir = f'../../code/output_our/{dataset_type}/parsing_data/{test_case_type}'
    else:
        data_load_root = f'../../code/output_base/{dataset_type}/inference/{test_case_type}/{model_name}/generated_step_all.json'
        output_dir = f'../../code/output_base/{dataset_type}/parsing_data/{test_case_type}'
    

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(
        output_dir,
        f'{model_name}-generated_step_all.json'
    )
    return pwd, data_load_root, output_path

def data_load(path):
    if path.endswith(".jsonl"):              # ChatGPT case
            records = []
            with open(path, encoding="utf-8") as f:
                for line in f:
                    if not line.strip():         # skip empty line
                        continue
                    rec = json.loads(line)
                    records.append(rec)

            problems = []
            for rec in records:
                try:
                    problems.append({
                        "task_id": [rec["name"]],
                        "outputs": [rec["grammar"][0]["production"][0]],
                        "contracts_list": rec["grammar"][0]["constraints"][0]
                    })
                except:
                    pdb.set_trace()
            return problems

    else:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
          
def clean_python_to_json_string(s):
    # 1) mask apostrophe and double-quote in explanation
    def _mask(m):
        inner = m.group(2)
        # " in explanation → \"
        inner = inner.replace('"', '\\"')
        # ' in explanation → __APOS__
        inner = inner.replace("'", "__APOS__")
        return f'{m.group(1)}{inner}{m.group(3)}'
    
    s = re.sub(
        r'("explanation"\s*:\s*")(.+?)(")',
        _mask,
        s,
        flags=re.DOTALL
    )

    # 2) Python literal → JSON literal
    s = s.replace("None", "null")
    s = s.replace("True", "true")
    
    s = s.replace("\\w", "\\\\w")
    s = s.replace("\\W", "\\\\W")
    s = s.replace("\\d", "\\\\d")
    s = s.replace("\\D", "\\\\D")
    s = s.replace("\\s", "\\\\s")
    s = s.replace("\\S", "\\\\S")
    s = s.replace("\\{", "\\\\{")
    s = s.replace("\\}", "\\\\}")
    s = s.replace("\\[", "\\\\[")
    s = s.replace("\\]", "\\\\]")
    s = s.replace("\\(", "\\\\(")
    s = s.replace("\\)", "\\\\)")
    s = s.replace("\\+", "\\\\+")
    s = s.replace("\\*", "\\\\*")
    s = s.replace("\\?", "\\\\?")
    s = s.replace("\\|", "\\\\|")
    s = s.replace("\\.", "\\\\.")
    s = s.replace("False", "false")

    # 3) remaining single-quote → double-quote  (JSON standard)
    s = s.replace("'", '"')

    # 4) unmask apostrophe
    s = s.replace("__APOS__", "'")

    return s



def wrap_section_fields(text):
    """
    wrap the value in the "input" → "explanation" section with json.dumps().
    """
    pattern = re.compile(
        r'("input"\s*:\s*)(.*?)'      # input: from the end
        r'(?=,\s*"explanation")',     # before explanation
        flags=re.DOTALL
    )
    def repl(m):
        prefix, snippet = m.group(1), m.group(2).strip()
        return prefix + json.dumps(snippet)
    return pattern.sub(repl, text)


def remove_inline_comments(text: str) -> str:
    """
    remove the text after '#' and '//' in each line, if it is not in the string literal.
    """
    lines = text.splitlines()
    new_lines = []

    for line in lines:
        in_str = False
        str_char = None
        clean = []
        i = 0
        while i < len(line):
            ch = line[i]
            # toggle string start/end
            if ch in ('"', "'"):
                if not in_str:
                    in_str = True
                    str_char = ch
                elif str_char == ch and line[i-1] != '\\':
                    in_str = False
                clean.append(ch)
                i += 1
            # '//' comment
            elif not in_str and ch == '/' and i+1 < len(line) and line[i+1] == '/':
                break  # remaining part is all comment
            # '#' comment
            elif not in_str and ch == '#':
                break
            else:
                clean.append(ch)
                i += 1

        new_lines.append(''.join(clean))
    return "\n".join(new_lines)


def remove_trailing_commas(text):
    return re.sub(r',\s*(?=[}\]])', '', text)



def fix_bracket_balance_for_string(val):
    """
    if the string looks like a list, fix the bracket balance or structure.
    if the list is already valid, leave it as is.
    """
    if isinstance(val, str) and val.strip().startswith('('):
        val = val.replace('(', '[').replace(')', ']')
    
    if not isinstance(val, str) or not val.strip().startswith('['):
        return val

    val_strip = val.strip()

    # 1. if the string can be parsed as a list, leave it as is
    try:
        parsed = ast.literal_eval(val_strip)
        if isinstance(parsed, (list, tuple)):
            return val_strip
    except Exception:
        pass

    # 2. fix the bracket balance
    open_sq = val_strip.count('[')
    close_sq = val_strip.count(']')
    if open_sq > close_sq:
        val_strip += ']' * (open_sq - close_sq)
    elif close_sq > open_sq:
        val_strip = '[' * (close_sq - open_sq) + val_strip

    # 3. try again
    try:
        parsed = ast.literal_eval(val_strip)
        if isinstance(parsed, (list, tuple)):
            return val_strip
    except Exception:
        pass

    # 4. last fallback: wrap the string with [] (except for already wrapped strings)
    if val_strip.startswith('[') and val_strip.endswith(']'):
        return val_strip  # avoid double wrapping
    return f'[{val_strip}]'


def excape_explanation(section):
    if section.find("\"explanation\"") != -1:
        end_idx = section.find("\"explanation\"")
    elif section.find("\"Explanation") != -1:
        end_idx = section.find("\"Explanation")
    else:
        end_idx = section.rfind("}")
    
    return section[:end_idx] + "\"explanation\": \"MISSING\"}"




def stringify_input_value(src: str) -> str:
    """
    {"input": [(), 2], "explanation": …}
         └─ depth calculation ─────┘
    → {"input": "[(), 2]", "explanation": …}

    • correctly recognize nested []
    • automatically insert comma after input
    • escape \" \\ inside
    """
    out, i, n = [], 0, len(src)

    while True:
        m = re.search(r'"input"\s*:\s*\[', src[i:])
        if not m:                         # no more
            out.append(src[i:])
            break

        # copy the beginning part as is
        start = i + m.start()
        arr_beg = i + m.end() - 1         # first '[' position
        out.append(src[i:start])

        # ── ① calculate the depth of the bracket ───────────────────────────
        depth, j = 0, arr_beg
        while j < n:
            ch = src[j]
            if ch == '[':
                depth += 1
            elif ch == ']':
                depth -= 1
                if depth == 0:
                    break
            elif ch == '"' and src[j-1] != '\\':
                # skip if [ ] is in the string
                k = j + 1
                while k < n and not (src[k] == '"' and src[k-1] != '\\'):
                    k += 1
                j = k
            j += 1
        if depth != 0:          # mismatch → leave as is and exit
            out.append(src[start:])
            break
        arr_end = j
        raw_arr = src[arr_beg:arr_end + 1]

        # ── ② array → JSON-safe string ───────────────────
        esc_arr = raw_arr.replace('\\', r'\\').replace('"', r'\"')
        repl = f'"input": "{esc_arr}"'

        # ── ③ if there is no comma after the array, fix it ───────────────────
        k = arr_end + 1
        tail_ws = []
        while k < n and src[k].isspace():
            tail_ws.append(src[k]); k += 1
        if k >= n or src[k] != ',':
            repl += ','                     # automatically insert comma
        out.append(repl + ''.join(tail_ws))

        # next search point
        i = k if k < n else n
        if i < n and src[i] == ',':         # if there is already a comma, copy it as is
            out.append(',')
            i += 1

    return ''.join(out)

def force_close_json(text):
    """
    • escape \n, \r, \t in the JSON string value
    • remove the trailing comma before closing the object or array
    • fix the bracket balance
    """
    # 1) value helper
    def _escape_ctrl(m):
        pre, body, suf = m.group(1), m.group(2), m.group(3)
        #body = body.replace('\\', '\\\\')
        body = body.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
        return f'{pre}{body}{suf}'

    # 2) escape-aware pattern to find the value string
    pattern = re.compile(
        r'(".*?":\s*")'        # group1: key": "
      + r'((?:\\.|[^"\\])*)'   # group2: \"…\"  include the escape also until the unescaped quote
      + r'(")',               # group3: closing quote
        flags=re.DOTALL
    )
    text = pattern.sub(_escape_ctrl, text)

    # 3) ,} or ,] → } or ]
    text = re.sub(r',\s*(?=[}\]])', '', text)

    # 4) fix the bracket balance
    o_b, c_b = text.count('{'), text.count('}')
    o_s, c_s = text.count('['), text.count(']')
    if o_b > c_b: text += '}'*(o_b-c_b)
    if o_s > c_s: text += ']'*(o_s-c_s)

    return text

def stringify_paren_input_value(src: str) -> str:
    """
    wrap the ("input": (…)) section with a string and make it JSON-safe.
    """
    out, i, n = [], 0, len(src)
    while True:
        m = re.search(r'"input"\s*:\s*\(', src[i:])
        if not m:
            out.append(src[i:])
            break

        start   = i + m.start()
        tup_beg = i + m.end() - 1     # first '(' position
        out.append(src[i:start])

        # ① calculate the depth of the bracket
        depth, j = 0, tup_beg
        while j < n:
            ch = src[j]
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
                if depth == 0:
                    break
            elif ch == '"' and src[j-1] != '\\':
                k = j + 1
                while k < n and not (src[k] == '"' and src[k-1] != '\\'):
                    k += 1
                j = k
            j += 1
        if depth != 0:               # mismatch
            out.append(src[start:])
            break

        tup_end = j
        raw_tup = src[tup_beg:tup_end + 1]

        # ② convert to JSON-safe string (None → null also)
        esc_tup = (
            raw_tup
            .replace('\\', r'\\')
            .replace('"',  r'\"')
            .replace('None', 'null')
        )
        
        repl = f'"input": "{esc_tup}"'

        # ③ fix the trailing comma
        k = tup_end + 1
        tail_ws = []
        while k < n and src[k].isspace():
            tail_ws.append(src[k]); k += 1
        if k >= n or src[k] != ',':
            repl += ','
        out.append(repl + ''.join(tail_ws))

        i = k if k < n else n
        if i < n and src[i] == ',':
            out.append(',')
            i += 1

    return ''.join(out)

def merge_orphan_values_in_input(text):
    """
    `"input": <token>, <orphan>, <orphan> … }`
    absorb the values joined by comma without key.
    safely handle any nested [] / {} / string / number.
    """
    out, i, n = [], 0, len(text)

    while True:
        p = text.find('"input"', i)
        if p == -1:                       # no more
            out.append(text[i:])
            break

        out.append(text[i:p])             # keep the part before "input"

        # find the first value after ':'
        j = text.find(':', p) + 1
        while j < n and text[j].isspace():
            j += 1

        # find the end of the first token (track the depth of [] / {} / string / number)
        depth = 0
        in_str = False
        k = j
        while k < n:
            ch = text[k]
            if ch == '"' and text[k-1] != '\\':
                in_str = not in_str
            elif not in_str:
                if ch in '[{':
                    depth += 1
                elif ch in ']}':
                    depth -= 1
                # when depth is 0 and meet `,` or `}`
                if (ch == ',' and depth == 0) or (ch == '}' and depth <= 0):
                    break
            k += 1
        first = text[j:k].strip()

        # collect the orphan values after the first token
        tail, t = [], k
        while True:
            while t < n and text[t].isspace():
                t += 1
            if t >= n or text[t] == '}':
                break
            if text[t] == ',':
                t += 1
            while t < n and text[t].isspace():
                t += 1

            start = t
            depth = 0
            in_str = False
            while t < n:
                ch = text[t]
                if ch == '"' and text[t-1] != '\\':
                    in_str = not in_str
                elif not in_str:
                    if ch in '[{':
                        depth += 1
                    elif ch in ']}':
                        depth -= 1
                    if (ch == ',' and depth == 0) or (ch == '}' and depth <= 0):
                        break
                t += 1
            tail.append(text[start:t].strip())

        # wrap the list
        # joined = ', '.join([first] + tail)
        # out.append(f'"input": [{joined}]')

        # wrap the list
        if not tail:                               # if there is no orphan value
            stripped = first.strip()
            # if the first token is already a list, leave it as is, otherwise wrap it once
            if stripped.startswith('[') and stripped.endswith(']'):
                out.append(f'"input": {stripped}')
            else:
                out.append(f'"input": [{stripped}]')
        else:                                      # if there is at least one orphan value
            joined = ', '.join([first] + tail)
            out.append(f'"input": [{joined}]')

        # keep the closing } and the trailing space/comma
        end_ptr = t
        if end_ptr < n:
            out.append(text[end_ptr])      # ‘}’
            end_ptr += 1
            while end_ptr < n and (text[end_ptr].isspace() or text[end_ptr] == ','):
                out.append(text[end_ptr])
                end_ptr += 1
        i = end_ptr

    return ''.join(out)


_INPUT_COMP_RE = re.compile(r'("input"\s*:\s*)(\[[^\]]*?for[^\]]*?\])')

def quote_input_expr(s):
    """
    wrap the "input": <python list/expression> section with a string so that it can be parsed by JSON.
    """
    key = '"input"'
    idx = s.find(key)
    if idx == -1:
        return s

    # find the position of '[' after ':' ignoring the trailing space
    colon = s.find(':', idx + len(key))
    i = colon + 1
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s) or s[i] != '[':
        return s

    # find the ']' corresponding to the depth counter (support nested list)
    depth = 0
    for j, ch in enumerate(s[i:], i):
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                end = j
                break
    else:
        return s  # if there is no closing bracket, do not change

    # include *, +, number, space, etc. after the list expression ends
    k = end + 1
    while k < len(s) and s[k] not in {',', '\n', '}'}:
        k += 1

    # safely escape the extracted expression by json.dumps
    expr = s[i:k].strip()
    safe = json.dumps(expr)

    # replace the original [ ... ]+... block with the safe string
    return s[:i] + safe + s[k:]

def unwrap_singleton_array(text):
    """
    flatten the 1-element array of '": [{' … '}]' format to an object.
    - keep the outer JSON structure, replace only when it is an only-one inner array.
    """
    # ①  ': [{'  →  ':{'
    text = re.sub(r'":\s*\[\s*{', '": {', text)
    # ②  '}]'  →  '}'
    text = re.sub(r'}\s*]', '}', text)
    return text

def extract_simplified_testcases(idx, raw_output, mode, contracts_list, model_name="not input model name"):
    """
    mode:
      - "section": parsing based on the original SECTION_NAMES
      - "assert": parsing based on the key of the actual data
    """
    normalized = raw_output
    if mode == 'functionality_specification': # functionality_specification
        # original way
        for sec in SECTION_NAMES:
            if isinstance(normalized, str):
                normalized = re.sub(rf"'{re.escape(sec)}'\s*:",f'"{sec}":',normalized)
            elif isinstance(normalized, list):
                normalized = re.sub(rf"'{re.escape(sec)}'\s*:",f'"{sec}":',normalized[0])
        simplified = {}
        for section in SECTION_NAMES:
            if f'\\"{section}\\"' in normalized:
                key_token =  f'\\"{section}\\"'
            else:
                key_token = f'"{section}"'
            key_idx   = normalized.find(key_token)
            if key_idx == -1:
                simplified[section] = []
                continue
            brace_open = normalized.find("{", key_idx)
            if brace_open == -1:
                simplified[section] = []
                continue
            depth = 0
            end_idx = None
            for i in range(brace_open, len(normalized)):
                if normalized[i] == "{":
                    depth += 1
                elif normalized[i] == "}":
                    depth -= 1
                    if depth == 0:
                        end_idx = i
                        break
            if end_idx is None:
                simplified[section] = []
                continue
            block = normalized[key_idx : end_idx + 1]
            section_json = "{" + block + "}"
            section_json = section_json.split("```")[0]  # remove code block
            section_json = section_json.replace(", ,", ",")  # remove duplicate comma
            section_json = remove_inline_comments(section_json)  # remove inline comments
            cleaned = clean_python_to_json_string(section_json)  # convert Python string to JSON string
            cleaned = wrap_section_fields(cleaned)  # wrap section fields
            cleaned = remove_trailing_commas(cleaned)  # remove trailing comma

            if 'ours' in model_name:            
                cleaned = unwrap_singleton_array(cleaned)
            cleaned = quote_input_expr(cleaned)
            try:
                parsed = json.loads(cleaned)  # JSON parsing
                tc = parsed.get(section, {})
                if tc:
                    input_val = tc.get("input")
                    input_val = fix_bracket_balance_for_string(input_val)  # ★ fix here!
                    simplified[section] = [{
                        "input": input_val,
                        # "expected_output": tc.get("expected_output"),
                        #"explanation": tc.get("explanation")
                    }]
                else:
                    simplified[section] = []
            except json.JSONDecodeError:
                try:
                    s = codecs.decode(cleaned, 'unicode_escape')
                    parsed = json.loads(s)
                    tc = parsed.get(section, {})
                    if tc:
                        input_val = tc.get("input")
                        input_val = fix_bracket_balance_for_string(input_val)
                        simplified[section] = [{
                            "input": input_val,
                            # "expected_output": tc.get("expected_output"),
                            #"explanation": tc.get("explanation")
                        }]
                    else:
                        simplified[section] = []
                except (json.JSONDecodeError, UnicodeDecodeError):
                    simplified[section] = []
        return simplified
    
    #########################################################
    elif mode == "assert_specification": # prior to assert_specification        
        for sec in contracts_list.keys():
            if isinstance(normalized, str):
                normalized = re.sub(rf"'{re.escape(sec)}'\s*:",f'"{sec}":',normalized)
            elif isinstance(normalized, list):
                normalized = re.sub(rf"'{re.escape(sec)}'\s*:",f'"{sec}":',normalized[0])
        simplified = {}
        for idx, section in enumerate(contracts_list.keys()):
            if f'\\"{section}\\"' in normalized:
                key_token =  f'\\"{section}\\"'
            else:
                key_token = f'"{section}"'
            key_idx   = normalized.find(key_token)
            if key_idx == -1:
                simplified[section] = []
                continue
            
            brace_open = normalized.find("{", key_idx)
            if brace_open == -1:
                simplified[section] = []
                continue
            
            
            # ── 2-A) find the next section ──────
           
            search_end = len(normalized)
            for other in contracts_list.keys():
                if int(section[-1])+1 != int(other[-1]):              # skip itself
                    continue
                nxt_pos = normalized.find(f'"{other}"', key_idx + len(key_token))
                if 0 <= nxt_pos < search_end:     # only select the nearest position
                    search_end = nxt_pos
            
            cursor = brace_open
            simplified[section] = []
            while cursor < search_end:
                if normalized[cursor] != "{":
                    cursor += 1
                    continue
            
                depth = 0
                start = cursor
                for j in range(cursor, search_end):
                    if normalized[j] == "{":
                        depth += 1
                    elif normalized[j] == "}":
                        depth -= 1
                        if depth == 0:            # complete one block
                            block = normalized[start : j + 1]
                            # ── 3) post-processing + JSON parsing ─────────────────
                            section_json = block.split("```")[0]        # remove code block
                            section_json = section_json.replace(", ,", ",")
                            section_json = remove_inline_comments(section_json)
                            section_json = clean_python_to_json_string(section_json)
                            section_json = wrap_section_fields(section_json)
                            section_json = remove_trailing_commas(section_json)
                            section_json = merge_orphan_values_in_input(section_json)
                            section_json = stringify_input_value(section_json)
                            section_json = stringify_paren_input_value(section_json) 
                            try:
                                section_json_fix = force_close_json(section_json)
                                parsed = json.loads(section_json_fix)
                                
                                inp = fix_bracket_balance_for_string(parsed.get("input"))
                                simplified[section].append({
                                    "input": inp,
                                    # "expected_output": tc.get("expected_output"),
                                    #"explanation": parsed.get("explanation", 'MISSING')
                                })
                            except json.JSONDecodeError:
                                try:
                                    raw = codecs.decode(section_json_fix, 'unicode_escape')
                                    parsed = json.loads(raw)
                                    
                                    inp = fix_bracket_balance_for_string(parsed.get("input"))
                                    simplified[section].append({
                                        "input": inp,
                                        # "expected_output": tc.get("expected_output"),
                                        #"explanation": parsed.get("explanation", 'MISSING')
                                    })
                                except (json.JSONDecodeError, UnicodeDecodeError):
                                    pass
                            cursor = j + 1        # move to the next block
                            break
                else:
                    # if the depth is not 0 until the end, exit the loop
                    break
        return simplified        
    
    #########################################################
    elif mode == "multi_assert_specification": # this cover combination of assert_specification
        # Extract all possible section keys (including combinations)
        all_sections = set()
        contracts_list = generate_contract_combinations(contracts_list)
        
        for sec in contracts_list.keys():
            all_sections.add(sec)
            # Add combination sections if they exist in the normalized text
            if isinstance(normalized, str):
                # Look for combination patterns like "assert_0,assert_1"
                combination_pattern = rf'"{re.escape(sec)},[^"]*"'
                matches = re.findall(combination_pattern, normalized)
                for match in matches:
                    # Extract the full combination key
                    full_key = match.strip('"')
                    all_sections.add(full_key)
            elif isinstance(normalized, list):
                combination_pattern = rf'"{re.escape(sec)},[^"]*"'
                matches = re.findall(combination_pattern, normalized[0])
                for match in matches:
                    full_key = match.strip('"')
                    all_sections.add(full_key)
        
        # Replace single quotes with double quotes for all sections
        for sec in all_sections:
            if isinstance(normalized, str):
                normalized = re.sub(rf"'{re.escape(sec)}'\s*:",f'"{sec}":',normalized)
            elif isinstance(normalized, list):
                normalized = re.sub(rf"'{re.escape(sec)}'\s*:",f'"{sec}":',normalized[0])
        
        simplified = {}
        for idx, section in enumerate(all_sections):
            if f'\\"{section}\\"' in normalized:
                key_token =  f'\\"{section}\\"'
            else:
                key_token = f'"{section}"'
            key_idx   = normalized.find(key_token)
            if key_idx == -1:
                simplified[section] = []
                continue
            
            brace_open = normalized.find("{", key_idx)
            if brace_open == -1:
                simplified[section] = []
                continue
            
            # ── 2-A) find the next section ──────
            search_end = len(normalized)
            for other in all_sections:
                # For combination sections, find the next section by position
                if section != other:
                    nxt_pos = normalized.find(f'"{other}"', key_idx + len(key_token))
                    if 0 <= nxt_pos < search_end:     # only select the nearest position
                        search_end = nxt_pos
            
            cursor = brace_open
            simplified[section] = []
            while cursor < search_end:
                if normalized[cursor] != "{":
                    cursor += 1
                    continue
            
                depth = 0
                start = cursor
                for j in range(cursor, search_end):
                    if normalized[j] == "{":
                        depth += 1
                    elif normalized[j] == "}":
                        depth -= 1
                        if depth == 0:            # complete one block
                            block = normalized[start : j + 1]
                            # ── 3) post-processing + JSON parsing ─────────────────
                            section_json = block.split("```")[0]        # remove code block
                            section_json = section_json.replace(", ,", ",")
                            section_json = remove_inline_comments(section_json)
                            section_json = clean_python_to_json_string(section_json)
                            section_json = wrap_section_fields(section_json)
                            section_json = remove_trailing_commas(section_json)
                            section_json = merge_orphan_values_in_input(section_json)
                            section_json = stringify_input_value(section_json)
                            section_json = stringify_paren_input_value(section_json) 
                            try:
                                section_json_fix = force_close_json(section_json)
                                parsed = json.loads(section_json_fix)
                                
                                inp = fix_bracket_balance_for_string(parsed.get("input"))
                                simplified[section].append({
                                    "input": inp,
                                })
                            except json.JSONDecodeError:
                                try:
                                    raw = codecs.decode(section_json_fix, 'unicode_escape')
                                    parsed = json.loads(raw)
                                    
                                    inp = fix_bracket_balance_for_string(parsed.get("input"))
                                    simplified[section].append({
                                        "input": inp,
                                    })
                                except (json.JSONDecodeError, UnicodeDecodeError):
                                    pass
                            cursor = j + 1        # move to the next block
                            break
                else:
                    # if the depth is not 0 until the end, exit the loop
                    break
        return simplified        
    
    else:
        raise ValueError("mode must be 'section' or 'assert'.")



if __name__ == "__main__":
    args = input_args()
    pwd, data_load_root, output_path = all_root(
        args.dataset_type, args.model_name, args.test_case_type
    )
    data = data_load(data_load_root)
    
    if args.model_name =='gpt-4o-mini':
        model_name = 'gpt-4o-mini'
        problems = data
    elif args.model_name == "o4-mini":
        model_name = 'o4-mini'
        problems = data
    elif "ours" in args.model_name:
        model_name = args.model_name
        problems = data
    else:
        model_name = list(data.keys())[1]
        problems = data[model_name]
    task_contracts_map = {p["task_id"][0]: p["contracts_list"] for p in problems} 
    nested_results = {}
    success_log = []
    failure_log = []

    for idx, item in enumerate(problems):
        if not item.get("outputs"):
            continue
        contracts_list = item["contracts_list"]
        raw_output = item["outputs"][0]
        parsed = extract_simplified_testcases(idx, raw_output, args.test_case_type, contracts_list, args.model_name)
        task_id = item.get("task_id")[0] if isinstance(item.get("task_id"), list) else item.get("task_id")
        if not any(parsed.values()):
            failure_log.append(task_id)
            continue
        
        success_log.append(task_id)
        nested_results.setdefault(model_name, {})[task_id] = parsed

    # 1) Save parsed JSON
    with open(output_path, "w") as f:
        json.dump(nested_results, f, indent=2)

    # 2) Append summary CSV
    summary_csv_path = output_path.replace(".json", "_summary_log.csv")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    success_str = ",".join(success_log)
    failure_str = ",".join(failure_log)

    # parsing is done, but calculate the number of tasks with all SECTION_NAMES filled
    complete_sections = 0
    for tid in success_log:                       # ★ problem_idx is not needed
        parsed = nested_results.get(model_name, {}).get(tid, {})
        contracts_list = task_contracts_map.get(tid)
        if contracts_list is None:                # in case of missing
            continue
        
        if 'contracts' in data_load_root or 'assert_specification' in data_load_root:
            if all(parsed.get(sec) for sec in contracts_list.keys()):
                complete_sections += 1
        else:
            if all(parsed.get(sec) for sec in SECTION_NAMES):
                complete_sections += 1
    
    incomplete_sections = len(success_log) - complete_sections

    write_header = not os.path.exists(summary_csv_path) or os.stat(summary_csv_path).st_size == 0
    with open(summary_csv_path, "a", newline="") as f:
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
        writer.writerow([
            timestamp,
            model_name,
            len(success_log),
            len(failure_log),
            success_str,
            failure_str,
            complete_sections,
            incomplete_sections
        ])

    # (Optional) print summary to the console
    print(f"[Summary] success={len(success_log)}, failure={len(failure_log)}, "
          f"all-sections-complete={complete_sections}, "
          f"par_tial={incomplete_sections}")
