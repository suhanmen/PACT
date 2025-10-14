def simplify(x, n):
    # Convert the strings to numerators and denominators
    x_num, x_denom = [int(val) for val in x.split('/')]
    n_num, n_denom = [int(val) for val in n.split('/')]
    
    # Multiply the fractions
    result_num = x_num * n_num
    result_denom = x_denom * n_denom
    
    # Check if the result is a whole number
    if result_num % result_denom == 0:
        return True
    else:
        return False
