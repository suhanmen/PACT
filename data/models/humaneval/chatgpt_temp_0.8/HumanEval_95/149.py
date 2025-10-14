def check_dict_case(dict):
    if len(dict) == 0:
        return False
    lower_keys = [key for key in dict.keys() if isinstance(key, str) and key.islower()]
    upper_keys = [key for key in dict.keys() if isinstance(key, str) and key.isupper()]
    if len(lower_keys) == len(dict) or len(upper_keys) == len(dict):
        return True
    else:
        return False
