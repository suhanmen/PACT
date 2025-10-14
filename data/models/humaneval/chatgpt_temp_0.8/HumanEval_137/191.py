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
    # convert inputs to tuples (value, type)
    a = (float(a.replace(',', '.')) if isinstance(a, str) else float(a), type(a))
    b = (float(b.replace(',', '.')) if isinstance(b, str) else float(b), type(b))

    # compare values based on their types
    if a[1] == b[1]:
        return max(a[0], b[0]) if a[0] != b[0] else None
    elif a[1] == int:
        return a[0] if a[0] > b[0] else b[0]
    elif b[1] == int:
        return b[0] if b[0] > a[0] else a[0]
    elif a[1] == float and b[1] == str:
        return a[0] if a[0] > b[0] else b[0]
    else:
        return b[0] if b[0] > a[0] else a[0]
