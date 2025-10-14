def is_prime(n):
    """Helper function that returns True if a number is prime, and False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Returns true if the given number is the multiplication of 3 prime numbers and false otherwise."""
    if a >= 100:
        return False
    primes = [i for i in range(2, 100) if is_prime(i)]
    prime_factors = []
    for p in primes:
        while a % p == 0:
            prime_factors.append(p)
            a //= p
    if len(prime_factors) == 3:
        return True
    else:
        return False
