def simplify(x, n):
    # convert the fractions to tuples of integers
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    
    # simplify the numerator and denominator of the product
    product_num = x_num * n_num
    product_denom = x_denom * n_denom
    
    # check if the product is a whole number
    if product_num % product_denom == 0:
        return True
    else:
        return False
