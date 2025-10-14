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
    if x == 0:  # special case for input number 0
        return '0'
    output = ''
    while x > 0:
        digit = x % base  # get the rightmost digit in the new base
        output = str(digit) + output  # append the new digit to the output string
        x //= base  # integer division to remove the rightmost digit
    return output
