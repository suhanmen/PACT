def check_dict_case(dict):
    if not dict: # check if the dictionary is empty
        return False
    lower = False
    upper = False
    for key in dict:
        if not isinstance(key, str): # check if the key is not a string
            return False
        if key.islower(): # check if the key is in lower case
            lower = True
        elif key.isupper(): # check if the key is in upper case
            upper = True
        else: # if the key is not in either cases, return False
            return False
    return lower != upper # check if either lower or upper is True, but not both
