def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, (int, float)):
            if a > b:
                return a
            elif a < b:
                return b
            else:
                return None
        elif isinstance(a, str) and ("," in a or "." in a):
            a = float(a.replace(",", ".")) if "," in a else float(a)
            b = float(b.replace(",", ".")) if "," in b else float(b)
            return compare_one(a, b)
        else:
            return None
    else:
        return None
