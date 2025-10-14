def check_dict_case(dict):
    if len(dict) == 0:
        return False
    lower_case = True
    upper_case = True
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.islower():
            upper_case = False
        elif key.isupper():
            lower_case = False
        else:
            return False
    return lower_case or upper_case
