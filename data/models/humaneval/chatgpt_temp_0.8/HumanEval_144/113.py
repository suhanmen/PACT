from fractions import Fraction

def simplify(x, n):
    x_val = Fraction(x)
    n_val = Fraction(n)
    product = x_val * n_val
    return product.denominator == 1
