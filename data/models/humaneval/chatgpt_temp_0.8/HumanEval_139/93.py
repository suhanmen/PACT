def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # initialize the result variable to 1
    result = 1
    
    # loop from n to 1 and multiply the factorial of each number
    for i in range(n, 0, -1):
        factorial_i = 1
        for j in range(i, 0, -1):
            factorial_i *= j
        result *= factorial_i

    # return the final result
    return result
