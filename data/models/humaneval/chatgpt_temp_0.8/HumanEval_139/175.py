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
    if n == 1:
        return 1
    
    # Calculate the regular factorial of n
    factorial_n = 1
    for i in range(1, n+1):
        factorial_n *= i
    
    # Calculate the Brazilian factorial
    brazilian_factorial = factorial_n
    for i in range(2, n+1):
        factorial_i = 1
        for j in range(1, i+1):
            factorial_i *= j
        brazilian_factorial *= factorial_i
    
    return brazilian_factorial
