def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Returns True if a is the multiplication of 3 prime numbers, False otherwise."""
    primes = []
    for i in range(2, a):
        if is_prime(i):
            primes.append(i)
            if len(primes) > 3:
                break
    if len(primes) == 3 and primes[0] * primes[1] * primes[2] == a:
        return True
    else:
        return False
