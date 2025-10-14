python
def prime_length(string):
    """
    Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    """
    # Check if the length of the string is less than or equal to 1
    if len(string) <= 1:
        return False
    # Check if the length of the string is 2
    elif len(string) == 2:
        return True
    # Check if the length of the string is divisible by any number from 2 to the length of the string - 1
    else:
        for i in range(2, len(string)):
            if len(string) % i == 0:
                return False
        return True
