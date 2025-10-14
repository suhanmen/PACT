def simplify(x, n):
    # Convert the strings to fractions
    x = Fraction(x)
    n = Fraction(n)
    # Multiply the fractions
    result = x * n
    # Check if the result is a whole number
    if result == result.numerator:
        return True
    else:
        return False
