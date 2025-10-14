def compare_one(a, b):
    try:
        a = float(a.replace(",", "."))
        b = float(b.replace(",", "."))
    except AttributeError:
        pass
    if type(a) == type(b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    else:
        return None
