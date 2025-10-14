def simplify(x, n):
    # Convert the strings x and n into numerators and denominators
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    
    # Multiply the two fractions
    result_num = x_num * n_num
    result_denom = x_denom * n_denom
    
    # Check if the result is a whole number
    return result_num % result_denom == 0
