def check_dict_case(dict):
    if not dict:
        return False
    lower = False
    upper = False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.islower():
            lower = True
        elif key.isupper():
            upper = True
        else:
            return False
    if lower and upper:
        return False
    return True
