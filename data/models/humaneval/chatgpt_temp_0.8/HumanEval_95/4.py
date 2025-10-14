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
    if not dict: # If dictionary is empty
        return False
    keys = list(dict.keys())
    case = None
    for key in keys:
        if not isinstance(key, str):
            return False
        if case is None: # If it's the first key we encounter
            if key.islower():
                case = 'lower'
            elif key.isupper():
                case = 'upper'
            else:
                return False
        else:
            if (case == 'lower' and key.isupper()) or (case == 'upper' and key.islower()):
                return False
    return True
