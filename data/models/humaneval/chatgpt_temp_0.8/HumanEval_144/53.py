def simplify(x, n):
    # Convert x and n to their corresponding numerators and denominators
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # Multiply the numerators and denominators
    result_num = x_num * n_num
    result_den = x_den * n_den
    
    # Check if the result is a whole number
    return result_num % result_den == 0
