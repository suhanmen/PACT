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
    # Initialize a variable to hold the special factorial
    special_fact = 1
    
    # Iterate from n to 1, multiplying each factorial by the special factorial
    for i in range(n, 0, -1):
        fact = 1
        for j in range(i, 0, -1):
            fact *= j
        special_fact *= fact
    
    # Return the special factorial
    return special_fact
