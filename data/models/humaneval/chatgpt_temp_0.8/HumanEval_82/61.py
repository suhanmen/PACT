import math

def is_prime(n):
    """Helper function to determine if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Returns True if the length of the string is a prime number, else False"""
    return is_prime(len(string))
