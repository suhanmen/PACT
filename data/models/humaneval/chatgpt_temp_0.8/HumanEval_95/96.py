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
    if len(dictionary) == 0:
        return False
    lowercase = 0
    uppercase = 0
    for key in dictionary.keys():
        if type(key) != str:
            return False
        if key.islower():
            lowercase += 1
        elif key.isupper():
            uppercase += 1
        else:
            return False
    if lowercase == 0 or uppercase == 0:
        return True
    else:
        return False
