def simplify(x, n):
    from fractions import Fraction
    # convert x and n to fractions
    x = Fraction(x)
    n = Fraction(n)
    # multiply x and n
    result = x * n
    # check if result is a whole number
    return result == int(result)
