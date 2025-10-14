def simplify(x, n):
    x_num, x_denom = x.split("/")
    n_num, n_denom = n.split("/")
    result_num = int(x_num) * int(n_num)
    result_denom = int(x_denom) * int(n_denom)
    if result_denom % result_num == 0:
        return True
    else:
        return False
