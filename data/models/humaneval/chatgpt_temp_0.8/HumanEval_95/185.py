def check_dict_case(dict):
    if len(dict) == 0:
        return False
    upper_keys = 0
    lower_keys = 0
    for key in dict.keys():
        if isinstance(key, str):
            if key.isupper():
                upper_keys += 1
            elif key.islower():
                lower_keys += 1
            else:
                return False
        else:
            return False
    return upper_keys == 0 or lower_keys == 0
