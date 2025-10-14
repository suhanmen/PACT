def simplify(x, n):
    # convert strings to integers
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    
    # multiply numerators and denominators
    num = x_num * n_num
    denom = x_denom * n_denom
    
    # check if result is a whole number
    return num % denom == 0
