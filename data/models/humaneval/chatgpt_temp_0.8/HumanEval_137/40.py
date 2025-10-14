def compare_one(a, b):
    if type(a) == type(b):
        if type(a) == int or type(a) == float:
            if a > b:
                return a
            elif b > a:
                return b
            else:
                return None
        elif type(a) == str:
            a_float = float(a.replace(",", "."))
            b_float = float(b.replace(",", "."))
            if a_float > b_float:
                return a
            elif b_float > a_float:
                return b
            else:
                return None
    else:
        return None
