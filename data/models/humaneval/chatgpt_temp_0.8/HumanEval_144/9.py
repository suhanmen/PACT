def simplify(x, n):
    x_num, x_den = [int(i) for i in x.split('/')]
    n_num, n_den = [int(i) for i in n.split('/')]
    result = x_num * n_num / (x_den * n_den)
    return result.is_integer()
