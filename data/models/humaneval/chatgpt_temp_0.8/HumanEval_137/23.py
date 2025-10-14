def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if type(a) != type(b):
        return None
    
    if isinstance(a, int) or isinstance(a, float):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, str):
        a = a.replace(",", ".") # replace , with .
        b = b.replace(",", ".")
        a_float = float(a)
        b_float = float(b)
        if a_float > b_float:
            return a
        elif a_float < b_float:
            return b
        else:
            return None
