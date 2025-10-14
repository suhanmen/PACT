def compare_one(a, b):
    if type(a) == type(b):
        if a == b:
            return None
        elif type(a) == int or type(a) == float:
            return max(a,b)
        elif type(a) == str:
            a_float = float(a.replace(",", "."))
            b_float = float(b.replace(",", "."))
            return b if a_float < b_float else a
    else:
        return None
