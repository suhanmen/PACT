def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    
    # Define a list of digits in the new base.
    digits = []
    
    # Divide x by the new base until it becomes 0.
    while x > 0:
        # Get the remainder of x when divided by the new base.
        remainder = x % base
        # Add the remainder to the list of digits.
        digits.append(str(remainder))
        # Divide x by the new base.
        x //= base
    
    # If x was 0 to start with, add a 0 to the list of digits.
    if len(digits) == 0:
        digits.append('0')
    
    # Reverse the list of digits and join them into a string.
    return ''.join(digits[::-1])
