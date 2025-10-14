def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n < 2: # Special cases for numbers less than 2
        return False
    elif n == 2: # Two is prime
        return True
    elif n % 2 == 0: # Any even number (except 2) is not prime
        return False
    else:
        # Check odd numbers up to the square root of n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
