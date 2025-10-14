import math

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise"""
    
    length = len(string)
    
    if length < 2: # Lengths of 0 and 1 are not prime
        return False
    
    if length == 2 or length == 3: # Lengths of 2 and 3 are prime
        return True
    
    if length % 2 == 0: # Even lengths are not prime
        return False
    
    for i in range(3, int(math.sqrt(length))+1, 2): # Check odd divisors up to sqrt of length
        if length % i == 0:
            return False
    
    return True
