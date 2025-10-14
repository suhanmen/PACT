# CANNOT PARSE CODE SNIPPET
def check_dict_case(d):
    if len(d) == 0:
        return False
    keys = list(d.keys())
    if all(k.islower() for k in keys) or all(k.isupper() for k in keys):
        return True
    else:
        return False
