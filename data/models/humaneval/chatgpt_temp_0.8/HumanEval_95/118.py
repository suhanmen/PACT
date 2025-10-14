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
    if len(dict) == 0:  # If dictionary is empty, return False
        return False
    
    lowercase_keys = 0
    uppercase_keys = 0
    
    for key in dict.keys():
        if not isinstance(key, str):  # If key is not a string, return False
            return False
        
        if key.islower():  # If key is lowercase, increment lowercase_keys
            lowercase_keys += 1
        elif key.isupper():  # If key is uppercase, increment uppercase_keys
            uppercase_keys += 1
        else:  # If key is not all lowercase or all uppercase, return False
            return False
    
    # If all keys are either all lowercase or all uppercase, return True
    return lowercase_keys == 0 or uppercase_keys == 0
