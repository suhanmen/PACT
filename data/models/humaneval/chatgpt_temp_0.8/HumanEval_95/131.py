def check_dict_case(dict):
    keys = dict.keys()
    if not keys:
        return False
    lower_case = all(key.islower() for key in keys)
    upper_case = all(key.isupper() for key in keys)
    return lower_case or upper_case
