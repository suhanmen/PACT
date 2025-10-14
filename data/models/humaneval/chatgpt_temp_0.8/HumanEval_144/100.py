def simplify(x, n):
    num_x, den_x = map(int, x.split("/"))
    num_n, den_n = map(int, n.split("/"))
    result = num_x * num_n / (den_x * den_n)
    return result.is_integer()
