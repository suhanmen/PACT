def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    result = ""
    while x >= base:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    result = str(x) + result
    return result
