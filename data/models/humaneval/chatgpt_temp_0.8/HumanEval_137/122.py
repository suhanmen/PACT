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
    if type(a) == type(b):
        if type(a) in [int, float]:
            return a if a > b else (b if b > a else None)
        elif type(a) == str:
            a = a.replace(",", ".")
            b = b.replace(",", ".")
            a_float = float(a)
            b_float = float(b)
            return a if a_float > b_float else (b if b_float > a_float else None)
    else:
        return None
