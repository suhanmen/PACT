def simplify(x, n):
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    product_num = int(x_num) * int(n_num)
    product_den = int(x_den) * int(n_den)
    return product_num % product_den == 0
