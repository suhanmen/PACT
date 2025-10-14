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
            a = a.replace(',', '.')
            b = b.replace(',', '.')
            a = float(a)
            b = float(b)
            if a > b:
                return str(a).replace('.', ',')
            elif b > a:
                return str(b).replace('.', ',')
            else:
                return None
    else:
        return None
