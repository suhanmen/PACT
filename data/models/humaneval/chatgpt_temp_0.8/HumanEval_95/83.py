# CANNOT PARSE CODE SNIPPET
def check_dict_case(dct):
    if not dct:
        return False
    lower_keys = [key for key in dct.keys() if isinstance(key, str) and key.islower()]
    upper_keys = [key for key in dct.keys() if isinstance(key, str) and key.isupper()]
    return len(lower_keys) == len(dct) or len(upper_keys) == len(dct)
