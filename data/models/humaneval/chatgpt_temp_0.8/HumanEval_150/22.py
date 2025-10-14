def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    # Check if n is a prime number
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                # If n is not prime, return y
                return y
        # If n is prime, return x
        return x
    # If n is not prime, return y
    return y
