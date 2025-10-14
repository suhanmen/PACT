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
    # Check if the dictionary is empty
    if not bool(dict):
        return False
    
    # Get the first key of the dictionary
    first_key = list(dict.keys())[0]
    
    # Check if all keys are lowercase strings
    if isinstance(first_key, str) and first_key.islower():
        for key in dict.keys():
            if not isinstance(key, str) or not key.islower():
                return False
        return True
    
    # Check if all keys are uppercase strings
    elif isinstance(first_key, str) and first_key.isupper():
        for key in dict.keys():
            if not isinstance(key, str) or not key.isupper():
                return False
        return True
    
    # Return False if keys are not all lowercase or all uppercase strings
    else:
        return False
