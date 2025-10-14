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

    # Convert a and b to floats if they are represented as strings
    if isinstance(a, str):
        a = float(a.replace(",", "."))
    else:
        a = float(a)

    if isinstance(b, str):
        b = float(b.replace(",", "."))
    else:
        b = float(b)

    # Compare a and b and return the larger variable in its given variable type
    if a > b:
        if isinstance(a, int):
            return a
        elif isinstance(a, float):
            return a
        else:
            return str(a)
    elif b > a:
        if isinstance(b, int):
            return b
        elif isinstance(b, float):
            return b
        else:
            return str(b)
    else:
        return None
