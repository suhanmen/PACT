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

    if not dict:
        return False

    lower_case = True
    upper_case = True

    for key in dict:
        if not isinstance(key, str):
            return False
        if key != key.lower():
            lower_case = False
        if key != key.upper():
            upper_case = False

    return lower_case or upper_case

# Test cases
print(check_dict_case({"a":"apple", "b":"banana"})) # should return True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # should return False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # should return False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # should return False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" })) # should return True