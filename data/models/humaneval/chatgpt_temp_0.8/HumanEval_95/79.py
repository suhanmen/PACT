def check_dict_case(dict):
    # Check if the dictionary is empty
    if not dict:
        return False
    
    # Check if all keys are in lower case or all keys are in upper case
    lower = all(key.islower() for key in dict.keys())
    upper = all(key.isupper() for key in dict.keys())
    
    return lower or upper
