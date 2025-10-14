def simplify(x, n):
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')
    res_num = int(x_num) * int(n_num)
    res_den = int(x_den) * int(n_den)
    return res_den % res_num == 0
