def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # First, check if the length of the string is less than 2
    # If it is, return False as neither 0 nor 1 are prime numbers
    if len(string) < 2:
        return False

    # Check if the length of the string is divisible by any number from 2 to the length of the string - 1
    for i in range(2, len(string)):
        if len(string) % i == 0:
            return False

    # If the length of the string is not divisible by any number from 2 to the length of the string - 1,
    # it is a prime number, so return True
    return True
