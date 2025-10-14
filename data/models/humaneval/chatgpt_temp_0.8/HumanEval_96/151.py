def count_up_to(n):
    """
    Return an array of the first n prime numbers less than n.
    """
    if n <= 1:
        return []

    primes = [2]
    num = 3

    while len(primes) < n and num < n:
        is_prime = True
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2

    return primes
