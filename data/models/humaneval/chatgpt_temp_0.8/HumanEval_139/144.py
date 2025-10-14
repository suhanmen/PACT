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

    # Initialize the result to 1
    result = 1
    
    # Loop through each number from 1 to n
    for i in range(1, n+1):
        # Calculate the factorial of i
        factorial_i = 1
        for j in range(1, i+1):
            factorial_i *= j
        
        # Multiply the result by the factorial of i
        result *= factorial_i
    
    # Return the result
    return result
