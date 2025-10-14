def simplify(x, n):
    # Convert x and n to their respective numerators and denominators
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    
    # Multiply the fractions
    result_num = x_num * n_num
    result_denom = x_denom * n_denom
    
    # Check if the result is a whole number
    if result_num % result_denom == 0:
        return True
    else:
        return False
