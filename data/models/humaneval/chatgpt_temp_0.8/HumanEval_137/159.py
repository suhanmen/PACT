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
    # Check if both variables are equal
    if str(a) == str(b):
        return None
    
    # Convert a and b to float if they are strings and contain , instead of .
    if isinstance(a, str) and ',' in a:
        a = float(a.replace(',', '.'))
    elif isinstance(a, str):
        a = float(a)
        
    if isinstance(b, str) and ',' in b:
        b = float(b.replace(',', '.'))
    elif isinstance(b, str):
        b = float(b)
    
    # Return the larger variable in its given variable type
    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    else:
        return max(str(a), str(b), key=float)
