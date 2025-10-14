def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n < 2: # 1 and negative numbers are not prime
        return False
    for i in range(2, int(n**(0.5))+1): # check for factors up to the square root of n
        if n % i == 0: # if n is divisible by a number other than 1 and itself, it's not prime
            return False
    return True
