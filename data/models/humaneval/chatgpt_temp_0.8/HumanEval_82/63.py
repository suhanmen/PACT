import math

def prime_length(string):
    length = len(string)
    if length < 2:  # special case of 0 or 1 length
        return False
    if length == 2:  # special case of 2 (the only even prime)
        return True
    if length % 2 == 0:  # all other even lengths are not prime
        return False
    for i in range(3, int(math.sqrt(length))+1, 2):
        if length % i == 0:
            return False
    return True
