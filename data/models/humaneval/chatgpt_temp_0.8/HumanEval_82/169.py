def is_prime(n):
    """Helper function that returns True if a number is prime or False otherwise"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Function that takes a string and returns True if the string length is a prime number or False otherwise"""
    length = len(string)
    return is_prime(length)
