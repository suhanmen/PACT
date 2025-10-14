def prime_length(string):
    # check if the length of the string is 1 or 0
    if len(string) < 2:
        return False
    
    # check if the length of the string is a prime number
    for i in range(2, int(len(string)**0.5)+1):
        if len(string) % i == 0:
            return False
    return True
