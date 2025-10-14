def check_dict_case(dict):
    if not dict:  # if the dictionary is empty
        return False
    
    # Check if all keys are strings and either all are in lower case or all are in upper case
    upper = False
    lower = False
    for key in dict.keys():
        if type(key) != str:
            return False
        elif key.isupper():
            upper = True
        elif key.islower():
            lower = True
        else:
            return False
    
    return not (upper and lower)  # Return True only if either all keys are upper case or all are lower case
