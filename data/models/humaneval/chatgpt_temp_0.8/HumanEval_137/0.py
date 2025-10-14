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

