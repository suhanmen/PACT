def simplify(x, n):
    # Convert x and n to floats
    x_float = float(eval(x))
    n_float = float(eval(n))
    
    # Multiply x and n
    result = x_float * n_float
    
    # Check if the result is an integer
    if result.is_integer():
        return True
    else:
        return False
