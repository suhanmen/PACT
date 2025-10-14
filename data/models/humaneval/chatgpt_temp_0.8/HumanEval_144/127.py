from fractions import Fraction

def simplify(x, n):
    x = Fraction(x)
    n = Fraction(n)
    result = x * n
    return result.denominator == 1
