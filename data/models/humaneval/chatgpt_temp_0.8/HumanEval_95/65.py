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
    if not my_dict: # if dictionary is empty
        return False
    lowercase = False
    uppercase = False
    for key in my_dict:
        if not isinstance(key, str): # if key is not a string
            return False
        if key.islower():
            lowercase = True
        elif key.isupper():
            uppercase = True
        else: # if key is neither all lower case nor all upper case
            return False
    return lowercase ^ uppercase # returns True if either of them is True, else False
