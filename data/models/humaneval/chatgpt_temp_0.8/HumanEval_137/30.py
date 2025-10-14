def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if type(a) != type(b):
        return None

    if isinstance(a, str):
        a = a.replace(",", ".")
        a = float(a)

    if isinstance(b, str):
        b = b.replace(",", ".")
        b = float(b)

    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b
