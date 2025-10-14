def is_prime(num):
    """Helper function to check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    """Function to check if string length is prime"""
    length = len(string)
    return is_prime(length)
