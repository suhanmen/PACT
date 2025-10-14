python
def multiply(a, b):
    """Takes two integers and returns the product of their unit digits."""
    # Get the unit digit of each input number
    a_unit = abs(a) % 10
    b_unit = abs(b) % 10
    # Calculate the product of the unit digits
    prod = a_unit * b_unit
    return prod
