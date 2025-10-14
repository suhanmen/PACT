from fractions import Fraction

def simplify(x, n):
    x_f = Fraction(x)
    n_f = Fraction(n)
    product = x_f * n_f
    return product.denominator == 1
