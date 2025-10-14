def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, str) and ("," in a or "." in a):
            a = float(a.replace(",", "."))
        if isinstance(b, str) and ("," in b or "." in b):
            b = float(b.replace(",", "."))
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    else:
        return None
