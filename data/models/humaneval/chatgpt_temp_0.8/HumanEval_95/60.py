def check_dict_case(dict):
    if len(dict) == 0:
        return False
    upper_case = False
    lower_case = False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.isupper():
            upper_case = True
        elif key.islower():
            lower_case = True
        else:
            return False
    return upper_case ^ lower_case
