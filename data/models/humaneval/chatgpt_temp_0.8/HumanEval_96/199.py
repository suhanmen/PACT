def count_up_to(n):
    """
    Returns an array of the first n integers that are prime numbers and less than n.
    """
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            if len(primes) == n:
                break
    return primes
