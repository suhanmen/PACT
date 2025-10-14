def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(",", ".") # replace comma with dot if present in string
    if isinstance(b, str):
        b = b.replace(",", ".") # replace comma with dot if present in string

    if type(a) != type(b):
        return None # return None if types are different

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None # return None if values are equal
