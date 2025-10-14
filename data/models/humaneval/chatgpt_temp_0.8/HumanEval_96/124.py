def is_prime(n):
    """Helper function to check if a number is prime or not."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
            if len(primes) == n:
                break
    return primes
