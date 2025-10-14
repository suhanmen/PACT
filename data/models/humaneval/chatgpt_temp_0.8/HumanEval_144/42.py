def simplify(x, n):
    x = x.split("/")
    n = n.split("/")
    numerator = int(x[0]) * int(n[0])
    denominator = int(x[1]) * int(n[1])
    if numerator % denominator == 0:
        return True
    else:
        return False
