def simplify(x, n):
    num_x, den_x = x.split('/')
    num_n, den_n = n.split('/')
    result = int(num_x) * int(num_n) / (int(den_x) * int(den_n))
    return result.is_integer()
