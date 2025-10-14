def largest_prime_factor(n: int):
    # Start with the smallest prime factor
    factor = 2
    # Keep dividing n by the current factor until it can't be divided anymore
    while n > factor:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    # The final value of factor is the largest prime factor
    return factor
