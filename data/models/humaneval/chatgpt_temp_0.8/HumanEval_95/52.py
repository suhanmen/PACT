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
    if len(dict) == 0:  # Return False if the dictionary is empty
        return False
    keys = list(dict.keys())  # Get a list of all the keys in the dictionary
    first_key = keys[0]  # Get the first key in the dictionary
    # Check if all keys are in lower case
    if all(type(key) == str and key.islower() for key in keys):
        return True
    # Check if all keys are in upper case
    elif all(type(key) == str and key.isupper() for key in keys):
        return True
    else:
        return False
