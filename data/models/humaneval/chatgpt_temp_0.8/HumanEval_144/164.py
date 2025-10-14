def simplify(x, n):
    x_num, x_denom = x.split("/")
    n_num, n_denom = n.split("/")
    
    result = int(x_num) * int(n_num) / (int(x_denom) * int(n_denom))
    return result.is_integer()
