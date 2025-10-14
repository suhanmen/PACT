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
    # Get the absolute value of a and b to handle negative numbers
    a = abs(a)
    b = abs(b)
    
    # Get the last digit of a and b
    a_last_digit = a % 10
    b_last_digit = b % 10
    
    # Return the product of the last digits
    return a_last_digit * b_last_digit
