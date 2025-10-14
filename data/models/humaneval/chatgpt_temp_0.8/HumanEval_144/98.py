from fractions import Fraction

def simplify(x, n):
    x_val = Fraction(x)
    n_val = Fraction(n)
    result = x_val * n_val
    return result.denominator == 1
