def is_prime(n):
    """Helper function to determine if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    primes = []
    i = 2
    while len(primes) < n and i < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes
