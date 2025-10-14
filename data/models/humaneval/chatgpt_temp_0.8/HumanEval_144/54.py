def simplify(x, n):
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    product = x_num * n_num / (x_denom * n_denom)
    return product.is_integer()
