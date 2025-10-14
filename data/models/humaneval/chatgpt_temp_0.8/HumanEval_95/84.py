def check_dict_case(dict):
    if len(dict) == 0:
        return False
    all_lower = all(key.islower() for key in dict.keys())
    all_upper = all(key.isupper() for key in dict.keys())
    if all_lower or all_upper:
        return True
    else:
        return False
