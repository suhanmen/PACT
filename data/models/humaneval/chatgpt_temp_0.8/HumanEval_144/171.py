from fractions import Fraction

def simplify(x, n):
    # convert both fractions to Fraction objects
    x = Fraction(x)
    n = Fraction(n)
    
    # multiply the fractions and simplify the result
    result = x * n
    result = result.limit_denominator()
    
    # check if the simplified result has a denominator of 1
    if result.denominator == 1:
        return True
    else:
        return False
