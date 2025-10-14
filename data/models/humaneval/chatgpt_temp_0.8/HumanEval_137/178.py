def compare_one(a, b):
    if type(a) != type(b):
        return None
    if isinstance(a, str):
        a = a.replace(",", ".")
        b = b.replace(",", ".")
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None
