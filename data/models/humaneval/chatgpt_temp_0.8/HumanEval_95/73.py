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
    
    if not dict: # if the dictionary is empty, return False
        return False
    
    keys = list(dict.keys()) # get a list of all keys
    
    # check if all keys are in lowercase
    if all(key.islower() for key in keys):
        return True
    
    # check if all keys are in uppercase
    elif all(key.isupper() for key in keys):
        return True
    
    # otherwise, return False
    else:
        return False
