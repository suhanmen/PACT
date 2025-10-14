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
    if type(a) == str and ',' in a:
        a = float(a.replace(',', '.'))
    elif type(a) != str:
        a = float(a)
        
    if type(b) == str and ',' in b:
        b = float(b.replace(',', '.'))
    elif type(b) != str:
        b = float(b)
        
    if a > b:
        if type(a) == int:
            return a
        elif type(a) == float:
            return round(a, 2)
        elif type(a) == str:
            return a
    elif b > a:
        if type(b) == int:
            return b
        elif type(b) == float:
            return round(b, 2)
        elif type(b) == str:
            return b
    else:
        return None
