def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    digits = "0123456789"
    if x < 0:
        sign = "-"
        x = -x
    else:
        sign = ""
    result = ""
    while x > 0:
        rem = x % base
        result = digits[rem] + result
        x = x // base
    return sign + result
