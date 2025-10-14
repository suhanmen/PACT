def simplify(x, n):
    # Convert the fractions to floats
    x_float = float(x.split('/')[0]) / float(x.split('/')[1])
    n_float = float(n.split('/')[0]) / float(n.split('/')[1])

    # Check if the product of the two floats is a whole number
    if x_float * n_float == int(x_float * n_float):
        return True
    else:
        return False
