def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if type(a) == type(b):
        if type(a) == int or type(a) == float:
            if a > b:
                return a
            elif b > a:
                return b
            else:
                return None
        elif type(a) == str:
            a = a.replace(",", ".")
            b = b.replace(",", ".")
            if float(a) > float(b):
                return a
            elif float(b) > float(a):
                return b
            else:
                return None
    else:
        return None
