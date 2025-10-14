def simplify(x, n):
    # Convert the fractions to floats
    x_float = float(x.split("/")[0]) / float(x.split("/")[1])
    n_float = float(n.split("/")[0]) / float(n.split("/")[1])
    
    # Multiply the fractions together and check if the product is a whole number
    product = x_float * n_float
    if product.is_integer():
        return True
    else:
        return False
