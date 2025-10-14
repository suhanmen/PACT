def compare_one(a, b):
    a_type = type(a)
    b_type = type(b)
    if a_type == b_type:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif a_type == int and b_type == float:
        return b
    elif a_type == float and b_type == int:
        return a
    elif a_type == str and b_type in [int, float]:
        a = float(a.replace(',', '.'))
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif b_type == str and a_type in [int, float]:
        b = float(b.replace(',', '.'))
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        return None
