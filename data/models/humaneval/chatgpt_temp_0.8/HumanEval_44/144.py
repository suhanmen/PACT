def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("base must be between 2 and 9")
    if x == 0:
        return '0'
    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x //= base
    return result
