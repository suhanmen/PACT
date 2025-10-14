def check_dict_case(dict):
    if not dict:
        return False
    lowercase_keys = all(key.islower() for key in dict.keys())
    uppercase_keys = all(key.isupper() for key in dict.keys())
    if lowercase_keys or uppercase_keys:
        return True
    else:
        return False
