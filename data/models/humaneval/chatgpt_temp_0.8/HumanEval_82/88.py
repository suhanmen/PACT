def is_prime(n):
    """Utility function to check if a number is prime or not"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Function to check if string length is prime"""
    length = len(string)
    return is_prime(length)
