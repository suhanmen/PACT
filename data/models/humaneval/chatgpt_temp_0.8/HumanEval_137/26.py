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
        if type(a) == int or type(a) == float:
            if a > b:
                return a
            elif a < b:
                return b
            else:
                return None
        elif type(a) == str:
            a = a.replace(",", ".")
            b = b.replace(",", ".")
            a = float(a)
            b = float(b)
            if a > b:
                return str(a).replace(".", ",")
            elif a < b:
                return str(b).replace(".", ",")
            else:
                return None
    else:
        return None
