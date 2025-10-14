def simplify(x, n):
    # Convert x and n to floats
    x_val = float(x.split('/')[0]) / float(x.split('/')[1])
    n_val = float(n.split('/')[0]) / float(n.split('/')[1])
    
    # Check if x * n is an integer
    if x_val * n_val == int(x_val * n_val):
        return True
    else:
        return False
