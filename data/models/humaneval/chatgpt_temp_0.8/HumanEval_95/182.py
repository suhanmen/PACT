def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict: # Return False if the dictionary is empty
        return False
    
    all_lower = True
    all_upper = True
    
    for key in dict.keys():
        if type(key) is not str: # If a key is not a string, return False
            return False
        elif not key.islower(): # If at least one key is not lowercase, set all_lower to False
            all_lower = False
        elif not key.isupper(): # If at least one key is not uppercase, set all_upper to False
            all_upper = False

    if all_lower or all_upper: # Return True if all keys are either lowercase or uppercase
        return True
    else:
        return False
