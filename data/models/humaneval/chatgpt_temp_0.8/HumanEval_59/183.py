def largest_prime_factor(n: int):
    # Start with the smallest prime factor, which is 2
    factor = 2
    # Keep track of the largest prime factor found so far
    largest_factor = 2
    # Keep dividing n by the smallest prime factor until it is no longer divisible
    while n > 1:
        if n % factor == 0:
            n //= factor
            largest_factor = factor
        else:
            # If the current factor doesn't divide n, try the next smallest prime factor
            factor += 1
    return largest_factor
