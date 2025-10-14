def is_prime(n):
    """A helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.
    
    Args:
    n (int): The number to check if it is prime.
    x (int): The value to return if n is prime.
    y (int): The value to return if n is not prime.
    
    Returns:
    int: The value of x if n is prime, otherwise the value of y.
    
    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime(n):
        return x
    else:
        return y
