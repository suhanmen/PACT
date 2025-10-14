def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # check if n is a prime number
    is_prime = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
    else:
        is_prime = False

    # return x if n is prime, y otherwise
    if is_prime:
        return x
    else:
        return y
