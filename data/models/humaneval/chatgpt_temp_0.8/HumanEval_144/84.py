def simplify(x, n):
    # Convert the fractions to floats and multiply them
    result = float(x) * float(n)
    
    # Check if the result is a whole number
    if result.is_integer():
        return True
    else:
        return False
