import math

def prime_length(string):
    """
    Takes a string and returns True if the string length is a prime number or False otherwise
    """
    string_length = len(string)
    
    # 1 and 2 are prime numbers
    if string_length == 1 or string_length == 2:
        return True
    
    # Check if string length is divisible by any number from 2 to its square root
    for i in range(2, int(math.sqrt(string_length))+1):
        if string_length % i == 0:
            return False
    
    return True
