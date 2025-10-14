def prime_length(string):
    """Returns True if the length of string is a prime number, False otherwise."""
    length = len(string)
    if length < 2:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True
