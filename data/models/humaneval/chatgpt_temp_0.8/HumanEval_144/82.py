def simplify(x, n):
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")
    # Multiply the two numerators and the two denominators
    numerator = int(x_numerator) * int(n_numerator)
    denominator = int(x_denominator) * int(n_denominator)
    # Check if the result is a whole number
    return numerator % denominator == 0
