# CANNOT PARSE CODE SNIPPET
def check_dict_case(d):
    if not d:  # empty dictionary
        return False
    lower_keys = 0
    upper_keys = 0
    for key in d.keys():
        if isinstance(key, str):
            if key.islower():
                lower_keys += 1
            elif key.isupper():
                upper_keys += 1
            else:  # mixed case string
                return False
        else:  # non-string key
            return False
    return lower_keys == len(d) or upper_keys == len(d)
