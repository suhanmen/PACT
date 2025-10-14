def count_up_to(n):
    """
    Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    """
    primes = []
    if n < 2:
        return primes
    primes.append(2)
    for num in range(3, n):
        is_prime = True
        for div in range(2, int(num**(0.5))+1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            if len(primes) == n:
                break
    return primes
