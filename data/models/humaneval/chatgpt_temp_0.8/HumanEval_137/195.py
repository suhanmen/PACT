def compare_one(a, b):
    a_type = type(a)
    b_type = type(b)

    if a_type == str:
        a = float(a.replace(",", "."))
    elif a_type != int and a_type != float:
        return None

    if b_type == str:
        b = float(b.replace(",", "."))
    elif b_type != int and b_type != float:
        return None

    if a == b:
        return None
    elif a > b:
        return a_type(a)
    else:
        return b_type(b)
