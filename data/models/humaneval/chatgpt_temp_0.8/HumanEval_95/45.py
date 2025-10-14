# CANNOT PARSE CODE SNIPPET
def check_dict_case(dictionary):
    if len(dictionary) == 0:  # if the dictionary is empty, return False
        return False
      
    lower_case = False
    upper_case = False
    for key in dictionary.keys():
        if not isinstance(key, str):  # if the key is not a string, return False
            return False
        if key.islower():  # check if all keys are in lower case
            lower_case = True
        elif key.isupper():  # check if all keys are in upper case
            upper_case = True
        else:  # if the key is not in upper or lower case, return False
            return False
    
    if lower_case and not upper_case:  # if all keys are in lower case and not in upper case, return True
        return True
    elif upper_case and not lower_case:  # if all keys are in upper case and not in lower case, return True
        return True
    else:
        return False  # if the dictionary has a mix of upper and lower case keys, return False
