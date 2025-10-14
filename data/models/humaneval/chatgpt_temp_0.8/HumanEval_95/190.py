def check_dict_case(dict):
    if len(dict) == 0:
        return False
    lowercase = 0
    uppercase = 0
    for key in dict.keys():
        if isinstance(key, str):
            if key.islower():
                lowercase += 1
            elif key.isupper():
                uppercase += 1
            else:
                return False
        else:
            return False
    if lowercase == len(dict) or uppercase == len(dict):
        return True
    else:
        return False
