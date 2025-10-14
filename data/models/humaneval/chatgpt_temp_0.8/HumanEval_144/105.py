def simplify(x, n):
    # Convert strings into fractions
    from fractions import Fraction
    x = Fraction(x)
    n = Fraction(n)
    
    # Compute product of fractions
    product = x * n
    
    # Check if product is a whole number
    if product.denominator == 1:
        return True
    else:
        return False
