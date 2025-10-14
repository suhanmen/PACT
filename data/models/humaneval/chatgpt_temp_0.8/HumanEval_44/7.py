def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x == 0:
        return '0'
    digits = []
    while x != 0:
        digits.append(str(x % base))
        x = x // base
    return ''.join(digits[::-1])
