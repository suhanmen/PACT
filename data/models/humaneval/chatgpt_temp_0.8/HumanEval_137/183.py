def compare_one(a, b):
    if type(a) != type(b): # check if the variables are of the same type
        return None
    if isinstance(a, str): # check if the variables are strings
        a = float(a.replace(',', '.')) # convert the string to a float and replace ',' with '.'
        b = float(b.replace(',', '.'))
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None
