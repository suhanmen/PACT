from fractions import Fraction

def simplify(x, n):
    x = Fraction(x)
    n = Fraction(n)
    product = x * n
    return product == int(product)
