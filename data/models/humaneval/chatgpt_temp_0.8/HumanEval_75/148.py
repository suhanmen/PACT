def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function that returns true if a is the multiplication of 3 prime numbers and false otherwise."""
    primes = []
    for i in range(2, a):
        if is_prime(i):
            primes.append(i)
    count = 0
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                if p1 * p2 * p3 == a:
                    count += 1
    return count == 1
