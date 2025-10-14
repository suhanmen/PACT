def check_dict_case(dict):
    if len(dict) == 0:
        return False
    lowercase_keys = 0
    uppercase_keys = 0
    for key in dict:
        if isinstance(key, str):
            if key.islower():
                lowercase_keys += 1
            elif key.isupper():
                uppercase_keys += 1
            else:
                return False
        else:
            return False
    if lowercase_keys > 0 and uppercase_keys > 0:
        return False
    else:
        return True
