def check_dict_case(dict):
    if len(dict) == 0:  # if the dictionary is empty, return False
        return False
    keys = list(dict.keys())  # get a list of all the keys
    if all(key.islower() for key in keys) or all(key.isupper() for key in keys):
        # check if all keys are either in lower case or in upper case
        return True
    else:
        return False
