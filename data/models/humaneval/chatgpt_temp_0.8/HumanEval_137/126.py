def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, (int, float)):
            if a > b:
                return a
            elif b > a:
                return b
            else:
                return None
        elif isinstance(a, str):
            a = a.replace(',', '.')
            b = b.replace(',', '.')
            a_float = float(a)
            b_float = float(b)
            if a_float > b_float:
                return a
            elif b_float > a_float:
                return b
            else:
                return None
    else:
        return None
