def prime_length(string):
    """
    Write a function that takes a string and returns True if the string length 
    is a prime number or False otherwise
    """
    length = len(string)
    if length <= 1:  # Length 0 and 1 are not prime
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True
