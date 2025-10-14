def compare_one(a, b):
    # Convert strings with , to .
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))

    # Compare variables based on their types
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif b > a:
            return b
    elif isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif b > a:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if a > b:
            return a
        elif b > a:
            return b

    # Return None if values are equal or cannot be compared
    return None
