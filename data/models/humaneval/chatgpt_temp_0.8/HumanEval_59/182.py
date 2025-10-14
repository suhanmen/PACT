def largest_prime_factor(n: int):
    # start with smallest prime factor
    factor = 2
    
    # keep dividing by factor until we can't anymore
    while factor <= n:
        if n % factor == 0:
            # found a factor, divide n by it and continue
            n //= factor
        else:
            # no factor, try the next one
            factor += 1
    
    # return the last factor we found, which is the largest prime factor
    return factor
