def check_dict_case(dict):
    if len(dict) == 0:
        return False
    lower_keys = all(key.islower() for key in dict.keys())
    upper_keys = all(key.isupper() for key in dict.keys())
    return lower_keys or upper_keys
