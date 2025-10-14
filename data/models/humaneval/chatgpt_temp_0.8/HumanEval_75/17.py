def is_prime(n):
    """Helper function that returns True if a number is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Returns True if a is the multiplication of 3 prime numbers, False otherwise."""
    if a < 2:
        return False
    primes = [i for i in range(2, a) if is_prime(i)]
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False
