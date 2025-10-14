# CANNOT PARSE CODE SNIPPET
def check_dict_case(my_dict):
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
    if not my_dict:  # if dictionary is empty, return False
        return False
    lowercase_keys = 0
    uppercase_keys = 0
    for key in my_dict.keys():
        if type(key) is not str:  # if a key is not a string, return False
            return False
        elif key.islower():  # if a key is lowercase, increment lowercase_keys
            lowercase_keys += 1
        elif key.isupper():  # if a key is uppercase, increment uppercase_keys
            uppercase_keys += 1
        else:  # if a key is neither uppercase nor lowercase, return False
            return False
    if lowercase_keys > 0 and uppercase_keys > 0: # if there are keys in both cases, return False
        return False
    return True  # if all keys are lowercase or uppercase, return True
