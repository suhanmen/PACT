def simplify(x, n):
    x_num, x_den = map(int, x.split('/')) # splitting x into numerator and denominator
    n_num, n_den = map(int, n.split('/')) # splitting n into numerator and denominator
    product = x_num * n_num / (x_den * n_den) # calculating the product of x and n
    return product.is_integer() # checking if the product is a whole number
