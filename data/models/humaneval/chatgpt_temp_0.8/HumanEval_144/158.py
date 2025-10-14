def simplify(x, n):
    x_parts = x.split('/')
    n_parts = n.split('/')
    num = int(x_parts[0]) * int(n_parts[0])
    den = int(x_parts[1]) * int(n_parts[1])
    gcd = math.gcd(num, den)
    if den // gcd == 1:
        return True
    else:
        return False
