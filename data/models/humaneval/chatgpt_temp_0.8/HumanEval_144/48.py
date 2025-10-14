def simplify(x, n):
    from fractions import Fraction
    # convert both fraction strings to fractions
    x = Fraction(x)
    n = Fraction(n)
    # multiply the fractions together
    result = x * n
    # check if the result is a whole number
    if result.denominator == 1:
        return True
    else:
        return False
