def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    """
    primes = []
    # An integer less than 2 is not a prime number
    if n < 2:
        return primes
    
    # Check for prime numbers up to n
    for num in range(2, n):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
            if len(primes) == n:
                return primes
    return primes
