import math

def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Function to check if length of string is prime"""
    length = len(string)
    if is_prime(length):
        return True
    else:
        return False
