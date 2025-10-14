python
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    upper = False
    lower = False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.islower():
            lower = True
        elif key.isupper():
            upper = True
        else:
            return False
    return upper ^ lower
