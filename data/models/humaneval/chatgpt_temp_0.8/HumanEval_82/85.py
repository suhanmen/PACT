import math

def prime_length(string):
    length = len(string)
    if length < 2:
        return False
    elif length == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(length))+1):
            if length % i == 0:
                return False
        return True
