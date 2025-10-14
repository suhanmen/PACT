def simplify(x, n):
    from fractions import Fraction
    x = Fraction(x)
    n = Fraction(n)
    product = x * n
    return product == int(product)
