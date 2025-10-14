def simplify(x, n):
    """
    Simplifies the expression x * n.

    :param x: string representation of a fraction
    :param n: string representation of a fraction
    :return: True if x * n evaluates to a whole number, False otherwise
    """
    # convert string fractions to numerator and denominator integers
    x_num, x_denom = map(int, x.split("/"))
    n_num, n_denom = map(int, n.split("/"))

    # multiply numerators and denominators
    product_num = x_num * n_num
    product_denom = x_denom * n_denom

    # simplify fraction by dividing numerator and denominator by their greatest common divisor
    gcd = math.gcd(product_num, product_denom)
    simplified_num = product_num // gcd
    simplified_denom = product_denom // gcd

    # check if simplified numerator is divisible by simplified denominator
    return simplified_num % simplified_denom == 0
