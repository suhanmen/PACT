def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n < 2: # 1 is not a prime number, and no number less than 2 is prime
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
