from fractions import Fraction

def simplify(x, n):
    x_fraction = Fraction(x)
    n_fraction = Fraction(n)
    product = x_fraction * n_fraction
    return product == int(product)
