def simplify(x, n):
    """
    Simplifies the expression x * n and returns True if it evaluates to a whole number, False otherwise.
    x and n are string representations of fractions in the format <numerator>/<denominator>, where both
    numerator and denominator are positive whole numbers.
    """
    # Convert string fractions to numerator and denominator integers
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    # Multiply numerator and denominator of both fractions
    result_num = int(x_num) * int(n_num)
    result_den = int(x_den) * int(n_den)
    # Check if result is a whole number
    if result_num % result_den == 0:
        return True
    else:
        return False
