from fractions import Fraction

def simplify(x, n):
    x_fraction = Fraction(x)
    n_fraction = Fraction(n)
    simplified = x_fraction * n_fraction
    return simplified.denominator == 1
