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
    if type(a) != type(b): # if the types of a and b are not the same, return None
        return None
    elif type(a) == str: # if the types of a and b are strings, convert them to floats
        try:
            a = float(a.replace(",", ".")) # replace "," with "." for decimal representation
            b = float(b.replace(",", "."))
        except ValueError: # if a or b cannot be converted to a float, return None
            return None
    if a == b: # if the values are equal, return None
        return None
    elif a > b:
        return a
    else:
        return b
