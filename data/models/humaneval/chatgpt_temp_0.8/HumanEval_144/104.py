def simplify(x, n):
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    if x_num * n_num % (x_denom * n_denom) == 0:
        return True
    else:
        return False
