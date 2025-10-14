def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(',', '.')
        a = float(a)
    if isinstance(b, str):
        b = b.replace(',', '.')
        b = float(b)
    if type(a) != type(b):
        return None
    elif a > b:
        return a
    elif b > a:
        return b
    else:
        return None
