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
    # Get the unit digit of a and b
    a_unit = abs(a) % 10
    b_unit = abs(b) % 10
    
    # Calculate the product of the unit digits
    product = a_unit * b_unit
    
    # Return the product
    return product
