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
    if len(dict) == 0: # check if dictionary is empty
        return False
    keys = list(dict.keys())
    first_key = keys[0]
    if isinstance(first_key, str): # check if first key is a string
        if first_key.isupper(): # check if first key is in upper case
            for key in keys[1:]:
                if not isinstance(key, str) or not key.isupper(): # check if all other keys are in upper case
                    return False
            return True
        elif first_key.islower(): # check if first key is in lower case
            for key in keys[1:]:
                if not isinstance(key, str) or not key.islower(): # check if all other keys are in lower case
                    return False
            return True
    return False # default case, return False
