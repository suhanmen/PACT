def simplify(x, n):
    x_numerator, x_denominator = map(int, x.split("/"))
    n_numerator, n_denominator = map(int, n.split("/"))
    product = x_numerator * n_numerator
    divisor = x_denominator * n_denominator
    gcd = 1
    for i in range(1, min(product, divisor) + 1):
        if product % i == 0 and divisor % i == 0:
            gcd = i
    product //= gcd
    divisor //= gcd
    return divisor == 1
