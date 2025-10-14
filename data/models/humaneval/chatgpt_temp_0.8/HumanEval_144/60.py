python
def simplify(x, n):
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    result = int(x_num) * int(n_num) / (int(x_den) * int(n_den))
    return result.is_integer()
