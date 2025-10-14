# CANNOT PARSE CODE SNIPPET
def check_dict_case(dictionary):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    """
    if not dictionary:
        return False  # return False if the dictionary is empty

    # create two sets to store keys in lower case and upper case
    keys_lower = set()
    keys_upper = set()

    for key in dictionary.keys():
        if not isinstance(key, str):
            return False  # return False if any key is not a string
        elif key.islower():
            keys_lower.add(key)  # add key to the set if it is in lower case
        elif key.isupper():
            keys_upper.add(key)  # add key to the set if it is in upper case
        else:
            return False  # return False if any key is neither in upper nor lower case

    # return True if all keys are in either lower case or upper case
    return len(keys_lower) == len(dictionary) or len(keys_upper) == len(dictionary)
