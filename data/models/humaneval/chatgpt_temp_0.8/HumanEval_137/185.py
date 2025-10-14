def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if type(a) == str and ',' in a:
        a = float(a.replace(',', '.'))
    else:
        a = float(a)
    if type(b) == str and ',' in b:
        b = float(b.replace(',', '.'))
    else:
        b = float(b)
    if a > b:
        if isinstance(a, int):
            return int(a)
        elif isinstance(a, float):
            return a
        else:
            return str(a)
    elif b > a:
        if isinstance(b, int):
            return int(b)
        elif isinstance(b, float):
            return b
        else:
            return str(b)
    else:
        return None
