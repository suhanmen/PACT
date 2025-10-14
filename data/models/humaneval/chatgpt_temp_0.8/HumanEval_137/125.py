def compare_one(a, b):
    # Convert strings to floats if they represent real numbers
    if isinstance(a, str):
        a = a.replace(',', '.')
        if '.' in a:
            a = float(a)
        else:
            a = int(a)
    if isinstance(b, str):
        b = b.replace(',', '.')
        if '.' in b:
            b = float(b)
        else:
            b = int(b)
    
    # Compare the values based on their variable type
    if type(a) == type(b):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        if isinstance(a, str) or isinstance(b, str):
            return max(str(a), str(b), key=float)
        else:
            return max(a, b)
