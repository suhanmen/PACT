def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    digits = "0123456789"
    result = ""
    while x > 0:
        remainder = x % base
        result = digits[remainder] + result
        x = x // base
    return result
