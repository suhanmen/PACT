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
    unit_a = abs(a) % 10
    unit_b = abs(b) % 10
    if unit_a == 0 or unit_b == 0:
        return 0
    product = unit_a * unit_b
    return product
