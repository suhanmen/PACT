def x_or_y(n, x, y):
    """
    A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.
    """
    if n < 2:
        return y
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return y
    return x
