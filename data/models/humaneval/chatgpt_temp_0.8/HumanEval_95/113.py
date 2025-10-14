def check_dict_case(dict):
    if len(dict) == 0:
        return False
    lower = False
    upper = False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        elif key.islower():
            lower = True
        elif key.isupper():
            upper = True
        else:
            return False
    return lower ^ upper
