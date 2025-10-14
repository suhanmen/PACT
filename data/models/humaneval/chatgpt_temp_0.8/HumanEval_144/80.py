def simplify(x, n):
    # convert the fractions to float values
    x_val = float(x.split("/")[0]) / float(x.split("/")[1])
    n_val = float(n.split("/")[0]) / float(n.split("/")[1])
    
    # check if the product is a whole number
    if x_val * n_val == int(x_val * n_val):
        return True
    else:
        return False
