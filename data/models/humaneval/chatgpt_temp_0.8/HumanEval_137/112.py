def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Convert a and b to floats if they are strings containing real numbers
    if isinstance(a, str) and ("," in a or "." in a):
        a = float(a.replace(",", "."))
    elif isinstance(a, str):
        a = float(a)
    if isinstance(b, str) and ("," in b or "." in b):
        b = float(b.replace(",", "."))
    elif isinstance(b, str):
        b = float(b)

    # Compare the values and return the larger variable in its given variable type
    if a > b:
        return a if isinstance(a, type(b)) else None
    elif b > a:
        return b if isinstance(b, type(a)) else None
    else:
        return None
