def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Get absolute value of a and b to avoid issues with negative numbers
    a = abs(a)
    b = abs(b)
    
    # Get the unit digits of a and b
    a_unit = a % 10
    b_unit = b % 10
    
    # Return the product of the unit digits
    return a_unit * b_unit
