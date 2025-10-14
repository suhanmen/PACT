def is_prime(n):
    """helper function that returns true if given number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise."""
    primes = []
    for i in range(2, a):
        if is_prime(i):
            primes.append(i)
            if len(primes) == 3:
                break
    if len(primes) != 3:
        return False
    else:
        return primes[0] * primes[1] * primes[2] == a
