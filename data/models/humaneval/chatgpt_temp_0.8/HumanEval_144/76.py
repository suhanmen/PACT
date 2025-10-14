def simplify(x, n):
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    
    # Check if the product of the numerators and denominators is a whole number
    if int(x_num) * int(n_num) % (int(x_den) * int(n_den)) == 0:
        return True
    else:
        return False
