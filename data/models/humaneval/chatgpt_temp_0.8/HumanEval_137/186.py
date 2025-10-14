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
    if isinstance(a, str):
        a = a.replace(",", ".")  # if a is a string, replace comma with dot
    if isinstance(b, str):
        b = b.replace(",", ".")  # if b is a string, replace comma with dot

    if type(a) != type(b):  # if a and b are not of the same type, return None
        return None

    if a == b:  # if a and b are equal, return None
        return None

    if a > b:
        return a
    else:
        return b
