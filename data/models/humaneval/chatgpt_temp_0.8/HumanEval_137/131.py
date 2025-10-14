def compare_one(a, b):
    if str(a).replace(',', '.') == str(b).replace(',', '.'): # convert commas to dots to handle string representation of floats
        return None
    elif isinstance(a, str) and isinstance(b, str): # both variables are strings
        if float(a.replace(',', '.')) > float(b.replace(',', '.')):
            return a
        else:
            return b
    elif isinstance(a, str):
        if float(a.replace(',', '.')) > b:
            return a
        else:
            return b
    elif isinstance(b, str):
        if a > float(b.replace(',', '.')):
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
