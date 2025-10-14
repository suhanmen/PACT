def is_prime(n):
    """Helper function to determine if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Return True if a is the multiplication of 3 prime numbers, False otherwise."""
    primes = [i for i in range(2, 100) if is_prime(i)]
    for i in primes:
        if a % i == 0:
            for j in primes:
                if j > i and a % (i * j) == 0:
                    for k in primes:
                        if k > j and a == i * j * k:
                            return True
    return False
