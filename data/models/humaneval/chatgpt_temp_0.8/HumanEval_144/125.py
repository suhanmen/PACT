def simplify(x, n):
    x_parts = x.split("/")
    n_parts = n.split("/")
    numerator = int(x_parts[0]) * int(n_parts[0])
    denominator = int(x_parts[1]) * int(n_parts[1])
    return numerator % denominator == 0
