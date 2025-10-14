import math

def is_prime(num):
    """Helper function to determine if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    """Function to check if a string's length is a prime number"""
    return is_prime(len(string))
