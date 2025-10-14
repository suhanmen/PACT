def simplify(x, n):
    from fractions import Fraction
    result = Fraction(x) * Fraction(n)
    return result.denominator == 1
