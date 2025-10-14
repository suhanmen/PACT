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
    if not dict:
        return False
    is_upper = None
    is_lower = None
    for key in dict.keys():
        if type(key) is not str:
            return False
        if key.islower():
            if is_upper is not None:
                return False
            is_lower = True
        elif key.isupper():
            if is_lower is not None:
                return False
            is_upper = True
        else:
            return False
    return True if is_upper is not None or is_lower is not None else False
