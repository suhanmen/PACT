def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, (int, float)):
            return a if a > b else b if b > a else None
        elif isinstance(a, str):
            a = a.replace(",", ".")
            b = b.replace(",", ".")
            return a if float(a) > float(b) else b if float(b) > float(a) else None
    else:
        return None
