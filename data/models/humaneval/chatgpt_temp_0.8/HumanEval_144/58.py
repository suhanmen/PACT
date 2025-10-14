def simplify(x, n):
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    product = x_num * n_num
    gcd = math.gcd(product, x_denom * n_denom)
    return (x_denom * n_denom) // gcd == product
