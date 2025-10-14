import math

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise"""
    
    length = len(string)
    
    if length < 2:
        return False
    
    for i in range(2, int(math.sqrt(length))+1):
        if length % i == 0:
            return False
        
    return True
