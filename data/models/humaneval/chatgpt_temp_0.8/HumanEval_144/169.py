def simplify(x, n):
    from fractions import Fraction
    # Convert the input fractions to Fraction objects
    x = Fraction(x)
    n = Fraction(n)
    # Multiply the fractions
    product = x * n
    # Check if the product is a whole number
    if product.denominator == 1:
        return True
    else:
        return False
