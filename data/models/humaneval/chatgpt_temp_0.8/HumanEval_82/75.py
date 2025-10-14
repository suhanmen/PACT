import math

def prime_length(string):
    """Determine if the length of a string is a prime number"""
    length = len(string)
    if length < 2:
        return False
    elif length == 2:
        return True
    else:
        # Check if length is divisible by any number up to sqrt(length)
        for i in range(2, int(math.sqrt(length)) + 1):
            if length % i == 0:
                return False
        return True
