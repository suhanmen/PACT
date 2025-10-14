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
    if not dict: # check if dictionary is empty
        return False
    
    keys = list(dict.keys())
    first_key = keys[0]
    if isinstance(first_key, str): # check if first key is a string
        if first_key.islower(): # check if first key is lowercase
            return all(key.islower() for key in keys) # check if all keys are lowercase
        elif first_key.isupper(): # check if first key is uppercase
            return all(key.isupper() for key in keys) # check if all keys are uppercase
    return False # if first key is not a string, return False
