def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    # Get largest non-zero coefficient
    a = None
    for coeff in reversed(xs):
        if coeff != 0:
            a = coeff
            break
    if a is None:
        return 0

    # Find all factors of a
    factors = []
    for i in range(1, int(math.sqrt(abs(a))) + 1):
        if a % i == 0:
            factors.append(i)
            factors.append(-i)
            factors.append(a // i)
            factors.append(-a // i)

    # Try all factor pairs as potential roots
    for i in range(0, len(factors), 2):
        x = (factors[i] + factors[i+1]) / 2
        if poly(xs, x) == 0:
            return x

    # If no root is found, return None
    return None
