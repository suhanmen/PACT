# CANNOT PARSE CODE SNIPPET
def check_dict_case(dictionary):
    """
    Given a dictionary, return True if all keys are strings in lower case
    or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """

    if not dictionary:  # If the dictionary is empty, return False
        return False

    keys = dictionary.keys()

    # Check if all keys are in lower case
    if all(key.islower() for key in keys):
        return True

    # Check if all keys are in upper case
    if all(key.isupper() for key in keys):
        return True

    # If neither all keys are in lower case nor all keys are in upper case, return False
    return False
