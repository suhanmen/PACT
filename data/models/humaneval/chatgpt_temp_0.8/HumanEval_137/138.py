def compare_one(a, b):
    if isinstance(a, str) and isinstance(b, str):
        a = float(a.replace(",", "."))
        b = float(b.replace(",", "."))
    elif isinstance(a, str):
        a = float(a.replace(",", "."))
    elif isinstance(b, str):
        b = float(b.replace(",", "."))
    
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None
