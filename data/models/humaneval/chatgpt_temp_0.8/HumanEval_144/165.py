def simplify(x, n):
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')
    try:
        result = int(x_num) * int(n_num) % (int(x_den) * int(n_den)) == 0
    except ZeroDivisionError:
        result = False
    return result
