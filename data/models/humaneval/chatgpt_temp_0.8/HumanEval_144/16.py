def simplify(x, n):
    # convert x and n to floats
    x_val = float(x.split('/')[0]) / float(x.split('/')[1])
    n_val = float(n.split('/')[0]) / float(n.split('/')[1])
    # multiply x and n
    result = x_val * n_val
    # check if the result is a whole number
    if result.is_integer():
        return True
    else:
        return False
