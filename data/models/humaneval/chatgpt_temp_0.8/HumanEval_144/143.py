def simplify(x, n):
    x_num, x_den = map(int, x.split("/"))  # numerator and denominator of x
    n_num, n_den = map(int, n.split("/"))  # numerator and denominator of n
    product = x_num * n_num  # product of numerators
    if product % (x_den * n_den) == 0:  # if product is divisible by the common denominator
        return True
    else:
        return False
