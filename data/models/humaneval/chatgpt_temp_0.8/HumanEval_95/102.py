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
    if not dict:  # Check if dictionary is empty
        return False
    
    lower_keys = 0
    upper_keys = 0
    
    for key in dict.keys():
        if not isinstance(key, str):  # Check if key is a string
            return False
        elif key.islower():  # Check if key is in lower case
            lower_keys += 1
        elif key.isupper():  # Check if key is in upper case
            upper_keys += 1
        else:  # Key has characters in mixed case
            return False
    
    if lower_keys > 0 and upper_keys > 0:  # Check if keys are in mixed case
        return False
    
    return True
