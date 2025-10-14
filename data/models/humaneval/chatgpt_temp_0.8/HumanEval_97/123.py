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
    abs_a = abs(a)
    abs_b = abs(b)
    unit_a = abs_a % 10
    unit_b = abs_b % 10
    return unit_a * unit_b
