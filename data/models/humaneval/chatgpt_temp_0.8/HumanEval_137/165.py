def compare_one(a, b):
    a_type = type(a)
    b_type = type(b)

    if a_type == str:
        a = float(a.replace(',', '.'))
    elif a_type not in [int, float]:
        return None

    if b_type == str:
        b = float(b.replace(',', '.'))
    elif b_type not in [int, float]:
        return None

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None
