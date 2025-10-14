from fractions import Fraction

def simplify(x, n):
    x_frac = Fraction(x)
    n_frac = Fraction(n)
    result = x_frac * n_frac
    if result.denominator == 1:
        return True
    else:
        return False
