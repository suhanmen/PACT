from fractions import Fraction

def simplify(x, n):
    x_fraction = Fraction(x)
    n_fraction = Fraction(n)
    result = x_fraction * n_fraction
    return result == int(result)
