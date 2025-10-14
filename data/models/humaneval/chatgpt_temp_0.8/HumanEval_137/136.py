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
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, str) or isinstance(b, str):
        a = a.replace(",", ".")
        b = b.replace(",", ".")
        if float(a) == float(b):
            return None
        elif float(a) > float(b):
            if isinstance(a, int):
                return a
            elif isinstance(a, float):
                return a
            else:
                return str(a)
        else:
            if isinstance(b, int):
                return b
            elif isinstance(b, float):
                return b
            else:
                return str(b)
    else:
        if a == int(a) and b == int(b):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        else:
            if isinstance(a, float):
                return a
            else:
  
