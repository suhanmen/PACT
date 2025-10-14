def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    # Return False if the given dictionary is empty
    if not dict:
        return False

    # Check if all keys are in upper case or lower case
    upper_case = all(key.isupper() for key in dict.keys())
    lower_case = all(key.islower() for key in dict.keys())

    # Return True if all keys are in upper case or lower case, else return False
    if upper_case or
