def prime_length(string):
    length = len(string)
    if length < 2:
        return False
    for number in range(2, int(length ** 0.5) + 1):
        if length % number == 0:
            return False
    return True
