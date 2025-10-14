def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise"""
    
    if len(string) < 2: # strings with length 0 or 1 are not prime
        return False
    for i in range(2, int(len(string) ** 0.5) + 1):
        if len(string) % i == 0:
            return False
    return True
