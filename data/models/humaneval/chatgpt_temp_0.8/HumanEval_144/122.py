def simplify(x, n):
    # convert strings to fractions
    from fractions import Fraction
    x = Fraction(x)
    n = Fraction(n)
    
    # multiply the fractions
    result = x * n
    
    # check if the result is a whole number
    if result.denominator == 1:
        return True
    else:
        return False
