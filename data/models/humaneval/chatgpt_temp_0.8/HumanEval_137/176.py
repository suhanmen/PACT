def compare_one(a, b):
    if type(a) == type(b):
        if isinstance(a, int) or isinstance(a, float):
            if a > b:
                return a
            elif b > a:
                return b
        elif isinstance(a, str):
            a = a.replace(',', '.')  # replace , with . to make it a valid float
            b = b.replace(',', '.')  # replace , with . to make it a valid float
            if float(a) > float(b):
                return a
            elif float(b) > float(a):
                return b
            else:
                return None
    else:
        return None
