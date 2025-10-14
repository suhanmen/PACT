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
    if not dict:  # check if dictionary is empty
        return False
    
    lower_keys = [key for key in dict.keys() if isinstance(key, str) and key.islower()]
    upper_keys = [key for key in dict.keys() if isinstance(key, str) and key.isupper()]
    
    return len(lower_keys) == len(dict) or len(upper_keys) == len(dict)
