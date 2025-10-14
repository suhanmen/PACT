def simplify(x, n):
    from fractions import Fraction
    x = Fraction(x)
    n = Fraction(n)
    result = x * n
    return result == int(result)
