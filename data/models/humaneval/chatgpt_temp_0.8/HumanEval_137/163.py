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

    # Convert string inputs to floats
    if isinstance(a, str):
        try:
            a = float(a.replace(',', '.'))
        except ValueError:
            return None

    if isinstance(b, str):
        try:
            b = float(b.replace(',', '.'))
        except ValueError:
            return None

    # Check if a and b are equal
    if a == b:
        return None

    # Return the larger value
    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, int):
        return a
    elif isinstance(a, int) and isinstance(b, float):
        return b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        return a
    elif isinstance(a, (int, float)) and isinstance(b, str):
        return b
