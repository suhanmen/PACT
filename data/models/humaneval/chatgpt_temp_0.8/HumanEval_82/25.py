def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # Check if string length is less than 2
    if len(string) < 2:
        return False

    # Check if string length is equal to 2
    if len(string) == 2:
        return True

    # Check if string length is divisible by 2
    if len(string) % 2 == 0:
        return False

    # Check if string length is divisible by any odd number less than itself
    for i in range(3, int(len(string)**0.5) + 1, 2):
        if len(string) % i == 0:
            return False

    return True
