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
    # Get the unit digit of both numbers
    a_unit = abs(a) % 10
    b_unit = abs(b) % 10
    
    # Check if any of the numbers is 0
    if a_unit == 0 or b_unit == 0:
        return 0
    
    # Multiply the unit digits and return the result
    result = a_unit * b_unit
    
    # Check if the result should be negative
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return -result
    
    return result
