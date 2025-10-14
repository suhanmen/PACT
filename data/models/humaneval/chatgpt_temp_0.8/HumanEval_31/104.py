def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i <= int(n ** 0.5) + 1:
            if n % i == 0:
                return False
            i += 2
        return True
