def prime_length(string):
    # Check if the length of the string is less than 2
    # If it is, the length is not a prime number
    if len(string) < 2:
        return False
    
    # Check if the length of the string is divisible by any number
    # between 2 and half the length of the string
    for i in range(2, len(string)//2 + 1):
        if len(string) % i == 0:
            return False
    
    # If the function hasn't returned False yet, the length of the string
    # is a prime number
    return True
