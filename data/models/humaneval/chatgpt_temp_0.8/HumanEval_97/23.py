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
    # Get the unit digits of both numbers
    a_unit = abs(a) % 10
    b_unit = abs(b) % 10
    
    # Check if either number is 0 or negative
    if a_unit == 0 or b_unit == 0:
        return 0
    elif a < 0:
        a_unit *= -1
    elif b < 0:
        b_unit *= -1
    
    # Return the product of the unit digits
    return a_unit * b_unit
