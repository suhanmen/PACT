def simplify(x, n):
    x_list = x.split("/")
    n_list = n.split("/")
    x_num = int(x_list[0])
    x_denom = int(x_list[1])
    n_num = int(n_list[0])
    n_denom = int(n_list[1])
    product_num = x_num * n_num
    product_denom = x_denom * n_denom
    gcd = math.gcd(product_num, product_denom)
    simplified_num = product_num // gcd
    simplified_denom = product_denom // gcd
    if simplified_denom == 1:
        return True
    else:
        return False
