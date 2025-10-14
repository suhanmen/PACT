def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1: # 1 is not a prime number
        return False
    # check for all numbers from 2 to the square root of n
    # if any of them divide n evenly, n is not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    # if we reach here, n is prime
    return True
