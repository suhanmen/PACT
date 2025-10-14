# CANNOT PARSE CODE SNIPPET
def check_dict_case(dictionary):
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
    if not dictionary:
        return False
    lowercase_keys = [key for key in dictionary.keys() if isinstance(key, str) and key.islower()]
    uppercase_keys = [key for key in dictionary.keys() if isinstance(key, str) and key.isupper()]
    if len(lowercase_keys) == len(dictionary) or len(uppercase_keys) == len(dictionary):
        return True
    else:
        return False
