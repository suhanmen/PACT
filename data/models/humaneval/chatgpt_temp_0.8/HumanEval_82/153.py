import math

def prime_length(string):
    string_length = len(string)
    if string_length <= 1:
        return False
    for i in range(2, int(math.sqrt(string_length)) + 1):
        if string_length % i == 0:
            return False
    return True
