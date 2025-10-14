def check_dict_case(dict):
    if len(dict) == 0:
        return False
    keys = list(dict.keys())
    first_key = keys[0]
    if first_key.islower():
        for key in keys:
            if not key.islower():
                return False
        return True
    elif first_key.isupper():
        for key in keys:
            if not key.isupper():
                return False
        return True
    else:
        return False
