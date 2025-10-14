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
    lowercase_count = 0
    uppercase_count = 0
    for key in dict.keys():
        if isinstance(key, str):
            if key.islower():
                lowercase_count += 1
            elif key.isupper():
                uppercase_count += 1
            else:
                return False
        else:
            return False
    if lowercase_count > 0 and uppercase_count == 0:
        return True
    elif uppercase_count > 0 and lowercase_count == 0:
        return True
    else:
        return False
