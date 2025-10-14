def compare_one(a, b):
    if type(a) != type(b):
        return None
    if type(a) == int or type(a) == float:
        if a > b:
            return a
        elif b > a:
            return b
    elif type(a) == str:
        if "." in a:
            a = a.replace(",", ".")
        elif "," in a:
            a = a.replace(",", ".")
        if "." in b:
            b = b.replace(",", ".")
        elif "," in b:
            b = b.replace(",", ".")
        a = float(a)
        b = float(b)
        if a > b:
            return str(a)
        elif b > a:
            return str(b)
    return None
