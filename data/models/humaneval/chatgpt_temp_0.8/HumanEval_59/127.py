def largest_prime_factor(n: int):
    factor = 2
    while n > factor:
        if n % factor == 0:
            n /= factor
        else:
            factor += 1
    return factor
