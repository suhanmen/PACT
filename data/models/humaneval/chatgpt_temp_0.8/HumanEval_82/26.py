import math

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string_length = len(string)
    if string_length <= 1:
        return False
    for i in range(2, int(math.sqrt(string_length))+1):
        if string_length % i == 0:
            return False
    return True
