import re

def check_str(string):
    pattern = r"^[aeiouAEIOU]"
    if re.match(pattern, string):
        return True
    else:
        return False

assert check_str("annie")