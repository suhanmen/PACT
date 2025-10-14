def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x < 0:
        return '-' + change_base(-x, base)
    result = ''
    while x >= base:
        result = str(x % base) + result
        x //= base
    result = str(x) + result
    return result
