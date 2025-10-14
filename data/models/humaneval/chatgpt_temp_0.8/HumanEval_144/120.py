def simplify(x, n):
    # Convert strings to fractions
    x_frac = Fraction(x)
    n_frac = Fraction(n)
    # Multiply fractions
    result = x_frac * n_frac
    # Check if result is a whole number
    if result.denominator == 1:
        return True
    else:
        return False
