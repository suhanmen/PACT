def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, (int, float)):
            if a > b:
                return a
            elif b > a:
                return b
        elif isinstance(a, str):
            a = a.replace(",", ".")
            b = b.replace(",", ".")
            if float(a) > float(b):
                return a
            elif float(b) > float(a):
                return b
        else:
            return None
    else:
        return None
