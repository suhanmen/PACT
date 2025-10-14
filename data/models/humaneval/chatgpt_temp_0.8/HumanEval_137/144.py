def compare_one(a, b):
    # convert strings with "," to floats
    if isinstance(a, str) and "," in a:
        a = float(a.replace(",", "."))
    if isinstance(b, str) and "," in b:
        b = float(b.replace(",", "."))

    if type(a) != type(b):
        return None
    elif a > b:
        return a
    elif b > a:
        return b
    else:
        return None
