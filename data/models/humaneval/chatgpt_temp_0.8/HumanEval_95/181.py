# CANNOT PARSE CODE SNIPPET
def check_dict_case(dictionary):
    if len(dictionary) == 0:  # if the dictionary is empty, return False
        return False
    
    keys = list(dictionary.keys())
    first_key_case = keys[0].islower()  # check if the first key is in lower case or not
    
    for key in keys:
        if key.islower() != first_key_case:  # if the current key is not in the same case as the first key, return False
            return False
    
    return True  # if all keys are in the same case, return True
