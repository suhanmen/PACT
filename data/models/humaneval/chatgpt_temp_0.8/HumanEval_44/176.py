def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    res = ""
    while x > 0:
        rem = x % base
        res = str(rem) + res
        x //= base
    return res
