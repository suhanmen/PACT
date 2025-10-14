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
    
    if not bool(dict): # check if dictionary is empty
        return False
    
    lowercase_keys = 0
    uppercase_keys = 0
    
    for key in dict.keys():
        if isinstance(key, str): # check if key is a string
            if key.islower():
                lowercase_keys += 1
            elif key.isupper():
                uppercase_keys += 1
            else:
                return False
        else:
            return False
    
    if lowercase_keys == 0 or uppercase_keys == 0: # check if all keys are either lower or upper case
        return True
    else:
        return False
