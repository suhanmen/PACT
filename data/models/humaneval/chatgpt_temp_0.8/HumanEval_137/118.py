def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, str):
            if '.' in a or ',' in a:
                a = float(a.replace(',', '.'))
            else:
                a = int(a)
            if '.' in b or ',' in b:
                b = float(b.replace(',', '.'))
            else:
                b = int(b)
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    else:
        return None
