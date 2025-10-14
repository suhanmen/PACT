def check_dict_case(dict):
    if not dict:   # check if the dictionary is empty
        return False  
    keys = list(dict.keys())
    first_key_case = keys[0].islower()  # check the case of the first key
    for key in keys:
        if key.islower() != first_key_case:  # check if the case of the current key matches the first key
            return False
        if not isinstance(key, str):  # check if the key is a string
            return False
    return True
