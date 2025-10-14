def check_dict_case(dict):
    if not dict:
        return False
    lowercase_keys = [key for key in dict.keys() if isinstance(key, str) and key.islower()]
    uppercase_keys = [key for key in dict.keys() if isinstance(key, str) and key.isupper()]
    if (len(lowercase_keys) == len(dict) or len(uppercase_keys) == len(dict)):
        return True
    else:
        return False
