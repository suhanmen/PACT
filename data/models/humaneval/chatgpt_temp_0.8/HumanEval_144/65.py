def simplify(x, n):
    from fractions import Fraction
    # Convert string representations of fractions to actual fractions
    x_frac = Fraction(x)
    n_frac = Fraction(n)
    # Multiply the fractions together
    product = x_frac * n_frac
    # Check if the product is a whole number
    return product.numerator % product.denominator == 0
