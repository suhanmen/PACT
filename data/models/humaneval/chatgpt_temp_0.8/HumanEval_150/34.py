def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 2: # 2 is the only even prime number
        return x
    elif n < 2 or n % 2 == 0: # all even numbers and 1 are not primes
        return y
    else:
        for i in range(3, int(n**0.5) + 1, 2): # check odd numbers up to sqrt(n)
            if n % i == 0:
                return y
        return x
