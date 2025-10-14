def is_multiply_prime(a):
    if a <= 1:
        return False

    # Find the prime factors of a
    factors = []
    d = 2
    while d*d <= a:
        while (a % d) == 0:
            factors.append(d)
            a //= d
        d += 1

    if a > 1:
        factors.append(a)

    # Check if we have 3 prime factors
    if len(factors) != 3:
        return False

    for factor in factors:
        if not is_prime(factor):
            return False

    return True
