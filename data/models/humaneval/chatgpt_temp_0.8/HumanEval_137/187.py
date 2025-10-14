def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    a_type, b_type = type(a), type(b)

    if a_type == b_type:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif a_type == str:
        a = float(a.replace(",", "."))
        if a > b:
            return str(a).replace(".", ",")
        elif a < b:
            return b
        else:
            return None
    elif b_type == str:
        b = float(b.replace(",", "."))
        if a > b:
            return a
        elif a < b:
            return str(b).replace(".", ",")
        else:
            return None
    elif a_type == int and b_type == float:
        if a > b:
            return a
        elif a < b:
     
