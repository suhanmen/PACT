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
        return False # return False if the dictionary is empty
    keys = list(dict.keys())
    first_key = keys[0]
    if first_key.islower(): # check if first key is in lower case
        return all(key.islower() for key in keys) # check if all keys are in lower case
    elif first_key.isupper(): # check if first key is in upper case
        return all(key.isupper() for key in keys) # check if all keys are in upper case
    else:
        return False # if first key is neither in upper nor lower case, return False
