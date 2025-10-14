# CANNOT PARSE CODE SNIPPET
def check_dict_case(dct):
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
    if not dct: # check if dictionary is empty
        return False
    lower_case = all(key.islower() for key in dct.keys()) # check if all keys are in lower case
    upper_case = all(key.isupper() for key in dct.keys()) # check if all keys are in upper case
    return lower_case or upper_case # return True if either condition is met, else False
