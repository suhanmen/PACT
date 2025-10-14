def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_up_to(n):
    """Return an array of the first n prime numbers less than n."""
    primes = []
    i = 2
    while len(primes) < n and i < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes
