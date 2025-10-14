def check_dict_case(dict):
    if not dict:  # if the dictionary is empty
        return False
    
    is_all_upper = True
    is_all_lower = True
    
    for key in dict.keys():
        if not isinstance(key, str):  # if the key is not a string
            return False
        if key.islower():
            is_all_upper = False
        elif key.isupper():
            is_all_lower = False
        else:
            return False
    
    return is_all_upper or is_all_lower  # if all keys are either upper or lower, return True, else False
