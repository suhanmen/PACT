def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x < 0: # Handle negative numbers
        sign = "-"
        x = abs(x)
    else:
        sign = ""
    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x //= base
    return sign + result
