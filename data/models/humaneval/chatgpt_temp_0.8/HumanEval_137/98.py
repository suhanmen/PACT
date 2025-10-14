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
    if type(a) == str and ("," in a or "." in a):
        a = a.replace(",", ".")
        a = float(a)
    else:
        a = float(a)
        
    if type(b) == str and ("," in b or "." in b):
        b = b.replace(",", ".")
        b = float(b)
    else:
        b = float(b)
        
    if a > b:
        if type(a) == int:
            return a
        elif type(a) == float:
            return "{:.1f}".format(a)
        else:
            return a
    elif b > a:
        if type(b) == int:
            return b
        elif type(b) == float:
            return "{:.1f}".format(b)
        else:
            return b
    else:
        return None
