import math

def is_prime(num):
    """Helper function to check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    """Function to check if the length of a string is a prime number"""
    length = len(string)
    return is_prime(length)
