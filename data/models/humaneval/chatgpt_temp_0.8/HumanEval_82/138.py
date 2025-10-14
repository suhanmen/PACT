def is_prime(n):
    """Helper function to determine if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Function to check if the length of a string is prime"""
    length = len(string)
    return is_prime(length)
