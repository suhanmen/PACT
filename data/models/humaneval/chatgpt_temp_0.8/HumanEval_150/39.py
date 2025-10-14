import math

def is_prime(n):
    """Check if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise."""
    if is_prime(n):
        return x
    else:
        return y
