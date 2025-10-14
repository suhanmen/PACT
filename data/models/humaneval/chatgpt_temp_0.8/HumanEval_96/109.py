def count_up_to(n):
    """
    Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    """
    primes = []
    for num in range(2, n):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
            if len(primes) == n:
                break
    return primes
