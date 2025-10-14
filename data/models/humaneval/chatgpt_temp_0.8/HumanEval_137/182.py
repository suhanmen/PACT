def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if isinstance(a, str) and isinstance(b, str):
        a = float(a.replace(",", "."))
        b = float(b.replace(",", "."))
    elif isinstance(a, str):
        a = float(a.replace(",", "."))
    elif isinstance(b, str):
        b = float(b.replace(",", "."))

    if type(a) != type(b):
        return None
    elif a == b:
        return None
    else:
        return max(a, b)
