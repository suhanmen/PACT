def simplify(x, n):
    # extract the numerators and denominators
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    # multiply the numerators and denominators
    product_num = x_num * n_num
    product_den = x_den * n_den
    # check if the product is a whole number
    return product_num % product_den == 0
