def simplify(x, n):
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    result = float(x_num) / float(x_den) * float(n_num) / float(n_den)
    return result.is_integer()
