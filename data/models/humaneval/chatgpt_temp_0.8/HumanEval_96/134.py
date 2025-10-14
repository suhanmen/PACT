def is_prime(n):
    """Helper function to check if a given number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Takes a non-negative integer n and returns an array of the first n prime numbers less than n"""
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
            if len(primes) == n:
                break
    return primes
