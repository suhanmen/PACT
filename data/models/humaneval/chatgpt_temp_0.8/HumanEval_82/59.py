import math

def prime_length(string):
    length = len(string)
    if length < 2:
        return False
    elif length == 2:
        return True
    elif length % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(length)) + 1, 2):
        if length % i == 0:
            return False
    return True
