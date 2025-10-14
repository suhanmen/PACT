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
    if not dict:  # Return False if dictionary is empty
        return False
    keys = list(dict.keys())  # Get list of dictionary keys
    first_key_case = keys[0].islower()  # Check if first key is lower case
    for key in keys[1:]:
        if key.islower() != first_key_case:
            return False  # If any other key case is different, return False
    return True  # If all keys have the same case, return True
