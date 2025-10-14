def compare_one(a, b):
    a_type = type(a)
    b_type = type(b)
    
    if a_type == str:
        a = a.replace(",", ".")
        a = float(a)
    else:
        a = float(a)
        
    if b_type == str:
        b = b.replace(",", ".")
        b = float(b)
    else:
        b = float(b)
    
    if a > b:
        return a_type(a)
    elif a < b:
        return b_type(b)
    else:
        return None
