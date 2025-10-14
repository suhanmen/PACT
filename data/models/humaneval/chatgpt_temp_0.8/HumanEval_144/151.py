def simplify(x, n):
    # Convert the strings to fractions using the Fraction module
    from fractions import Fraction
    x_fraction = Fraction(x)
    n_fraction = Fraction(n)
    
    # Multiply the fractions
    result = x_fraction * n_fraction
    
    # Check if the result is a whole number
    return result == int(result)
