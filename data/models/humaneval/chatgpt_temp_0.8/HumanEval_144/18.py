from fractions import Fraction

def simplify(x, n):
    x_f = Fraction(x)
    n_f = Fraction(n)
    result = x_f * n_f
    return result.denominator == 1
