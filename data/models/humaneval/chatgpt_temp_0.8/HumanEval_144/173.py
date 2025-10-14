def simplify(x, n):
    # Convert x and n to fractions and multiply them
    from fractions import Fraction
    result = Fraction(x) * Fraction(n)
    
    # Check if the result is a whole number
    if result.denominator == 1:
        return True
    else:
        return False
