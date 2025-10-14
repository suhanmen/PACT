# CANNOT PARSE
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
    
    if not bool(dict):
        return False # Return False if the dictionary is empty
    else:
        lowercase = True # Check if all keys are in lower case
        uppercase = True # Check if all keys are in upper case
        for key in dict.keys():
            if type(key) != str:
                return False # If the key is not a string, return False
            elif key.isupper():
                lowercase = False # If a key is in upper case, set lowercase to False
            elif key.islower():
                uppercase = False # If a key is in lower case, set uppercase to False
            else:
                return False # If the key is neither upper or lower case, return False
        return lowercase or uppercase # Return True if all keys are either in upper case or lower case.
