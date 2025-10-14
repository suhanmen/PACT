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
    # Initialize a list to store the digits of the new number in reverse order
    new_num = []
    
    # Perform the conversion
    while x > 0:
        digit = x % base
        new_num.append(str(digit))
        x //= base
    
    # Reverse the list and join the elements to create the string representation of the new number
    return ''.join(reversed(new_num))
