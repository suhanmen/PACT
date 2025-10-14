def largest_prime_factor(n: int):
    # Set initial factor to 2
    factor = 2
    # Keep dividing n by factor until it cannot be divided any further
    while n > factor:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    # The final value of factor is the largest prime factor of n
    return factor
