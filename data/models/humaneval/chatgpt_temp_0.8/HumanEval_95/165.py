def check_dict_case(dict):
    if len(dict) == 0:  # If the dictionary is empty, return False
        return False
    
    lower_keys = 0
    upper_keys = 0
    
    for key in dict.keys():
        if not isinstance(key, str):  # If the key is not a string, return False
            return False
        elif key.islower():  # If the key is in lower case, increment lower_keys
            lower_keys += 1
        elif key.isupper():  # If the key is in upper case, increment upper_keys
            upper_keys += 1
        else:  # If the key is neither upper nor lower case, return False
            return False
    
    if lower_keys == 0 or upper_keys == 0:  # If all keys are not in the same case, return False
        return True
    else:
        return False
