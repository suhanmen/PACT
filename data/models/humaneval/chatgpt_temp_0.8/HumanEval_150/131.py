def x_or_y(n, x, y):
    # Check if n is a prime number
    for i in range(2, n):
        if n % i == 0:
            return y
    
    # If n is not divisible by any number other than 1 and itself,
    # then it is a prime number
    return x
