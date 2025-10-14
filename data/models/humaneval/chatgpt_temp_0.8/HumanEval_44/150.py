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
    # Handle the case where x is 0
    if x == 0:
        return '0'

    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base

    # Reverse the list of digits and join them as a string
    return ''.join(digits[::-1])
