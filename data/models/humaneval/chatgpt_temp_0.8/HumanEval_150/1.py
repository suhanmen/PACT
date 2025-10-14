def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.
    
    """
    if n == 2:
        return x
    elif n < 2 or n % 2 == 0:
        return y
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return y
        return x
