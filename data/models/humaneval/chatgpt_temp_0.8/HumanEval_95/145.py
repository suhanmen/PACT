# CANNOT PARSE CODE SNIPPET
def check_dict_case(d):
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
    if len(d) == 0:
        return False
    keys = list(d.keys())
    first_key = keys[0]
    if isinstance(first_key, str):
        if first_key.islower():
            return all(k.islower() for k in keys)
        elif first_key.isupper():
            return all(k.isupper() for k in keys)
    return False
