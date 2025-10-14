def largest_prime_factor(n: int):
    # Start with 2 as the smallest prime factor
    factor = 2
    # Keep dividing n by the smallest prime factor until it cannot be divided anymore
    while n > factor:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    # The last factor we divided by is the largest prime factor
    return factor
