def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n < 2:  # 1 is not prime by definition
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # all other even numbers are not prime
        return False
    # check odd numbers up to the square root of n
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
