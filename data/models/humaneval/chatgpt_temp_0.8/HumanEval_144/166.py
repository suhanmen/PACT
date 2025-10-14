def simplify(x, n):
    from fractions import Fraction
    # convert string fractions to Fraction objects
    x = Fraction(x)
    n = Fraction(n)
    # multiply fractions
    result = x * n
    # check if result is a whole number
    return result == int(result)
