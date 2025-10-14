def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    product = x_num * n_num
    
    if product % (x_den * n_den) == 0:
        return True
    else:
        return False
