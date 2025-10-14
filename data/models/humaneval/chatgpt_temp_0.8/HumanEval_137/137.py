def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """

    # Check if the values are equal
    if a == b:
        return None

    # Convert strings to floats
    if type(a) == str:
        a = float(a.replace(",", "."))
    if type(b) == str:
        b = float(b.replace(",", "."))

    # Check which value is larger
    if type(a) == int and type(b) == int:
        return max(a, b)
    elif type(a) == float and type(b) == float:
        return max(a, b)
    elif type(a) == str and type(b) == str:
        return max(a, b)
    else:
        return None
