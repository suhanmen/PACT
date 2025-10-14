def compare_one(a, b):
    if type(a) != type(b):
        return None
    
    if isinstance(a, int) or isinstance(a, float):
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
    
    return None
