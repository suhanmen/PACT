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
    if a == b:
        return None
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return max(a, b)
        elif isinstance(b, str):
            if '.' in b or ',' in b:
                b = float(b.replace(',', '.'))
                return max(a, b)
    elif isinstance(a, str):
        if '.' in a or ',' in a:
            a = float(a.replace(',', '.'))
            if isinstance(b, int) or isinstance(b, float):
                return max(a, b)
            elif isinstance(b, str):
                if '.' in b or ',' in b:
                    b = float(b.replace(',', '.'))
                    return max(a, b)
                else:
                    return a
            else:
                return a
        else:
            if isinstance(b, str):
                return max(a, b)
            else:
                return None
    else:
        return None
