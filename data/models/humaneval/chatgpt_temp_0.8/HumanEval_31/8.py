def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n < 2:  # 1 is not prime, and no number less than 2 is prime
        return False
    for i in range(2, int(n**0.5) + 1):  # check divisors up to square root of n
        if n % i == 0:  # n is divisible by i, so it is not prime
            return False
    return True  # n is not divisible by any integer between 2 and its square root, so it is prime
