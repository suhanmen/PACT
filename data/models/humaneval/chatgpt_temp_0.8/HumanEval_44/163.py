def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    result = ''
    while x > 0:
        digit = x % base
        result = str(digit) + result
        x //= base
    return result
