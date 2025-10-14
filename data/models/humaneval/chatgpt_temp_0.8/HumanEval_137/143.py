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
            elif a < b:
                return b
            else:
                return None
        elif type(a) == str:
            float_a = float(a.replace(",", "."))
            float_b = float(b.replace(",", "."))
            if float_a > float_b:
                return a
            elif float_a < float_b:
                return b
            else:
                return None
    else:
        return None
