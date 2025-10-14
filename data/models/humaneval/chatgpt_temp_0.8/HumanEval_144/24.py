def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    product = num1 * num2
    divisor = den1 * den2
    gcd = math.gcd(product, divisor)
    return divisor // gcd == 1
