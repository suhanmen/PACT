def is_prime(n):
    """Helper function that takes a positive integer and returns True if it is prime, False otherwise."""
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Function that takes a non-negative integer and returns an array of the first n integers that are prime numbers and less than n."""
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
            if len(primes) == n:
                break
    return primes
