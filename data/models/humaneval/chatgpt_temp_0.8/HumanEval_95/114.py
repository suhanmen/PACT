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
    if len(dict) == 0:
        return False
    
    lower_keys = [k for k in dict.keys() if isinstance(k, str) and k.islower()]
    upper_keys = [k for k in dict.keys() if isinstance(k, str) and k.isupper()]
    
    if len(lower_keys) == len(dict) or len(upper_keys) == len(dict):
        return True
    else:
        return False
