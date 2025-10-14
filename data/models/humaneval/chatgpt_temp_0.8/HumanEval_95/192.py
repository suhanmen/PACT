# CANNOT PARSE CODE SNIPPET
def check_dict_case(my_dict):
    if not my_dict: # check if dictionary is empty
        return False
    lower = False
    upper = False
    for key in my_dict.keys():
        if not isinstance(key, str) or (key.islower() and upper) or (key.isupper() and lower):
            return False
        if key.islower():
            lower = True
        elif key.isupper():
            upper = True
    return lower != upper
