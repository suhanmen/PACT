def compare_one(a, b):
    # Convert strings with comma decimal separators to floats
    if isinstance(a, str) and "," in a:
        a = float(a.replace(",", "."))
    if isinstance(b, str) and "," in b:
        b = float(b.replace(",", "."))
    
    # Compare the values based on their variable type
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
    
    # Return None if the values are equal or cannot be compared
    return None
