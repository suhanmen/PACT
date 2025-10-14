def simplify(x, n):
    # Convert the string fractions to numeric values
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # Compute the multiplication of the fractions
    result_num = x_num * n_num
    result_den = x_den * n_den
    
    # Check if the result is a whole number
    is_whole = result_num % result_den == 0
    
    # Return the result
    return is_whole
