def is_multiply_prime(a):
    # Check if the input is less than 2 or not an integer
    if not isinstance(a, int) or a < 2:
        return False

    # Find the prime factors of the input number
    factors = []
    d = 2
    while d * d <= a:
        while (a % d) == 0:
            factors.append(d)
            a //= d
        d += 1
    if a > 1:
        factors.append(a)

    # Check if there are exactly 3 prime factors
    prime_factors = [f for f in factors if all(f % i != 0 for i in range(2, int(f ** 0.5) + 1))]
    return len(prime_factors) == 3
