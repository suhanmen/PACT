def is_prime(n):
    """returns True if n is a prime number, False otherwise"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """takes a string and returns True if the string length is a prime number"""
    return is_prime(len(string))
