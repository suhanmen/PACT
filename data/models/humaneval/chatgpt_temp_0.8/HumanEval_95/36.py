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
        # Check if the dictionary is empty
        return False
    lowercase_keys = 0
    uppercase_keys = 0
    for key in dict.keys():
        # Count the number of lowercase and uppercase keys
        if isinstance(key, str):
            if key.islower():
                lowercase_keys += 1
            elif key.isupper():
                uppercase_keys += 1
            else:
                # If a key is neither uppercase nor lowercase, return False
                return False
        else:
            # If a key is not a string, return False
            return False
    # Check if all keys are either lowercase or uppercase
    if lowercase_keys == len(dict) or uppercase_keys == len(dict):
        return True
    else:
        return False
