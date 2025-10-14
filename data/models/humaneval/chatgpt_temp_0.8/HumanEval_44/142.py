def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x == 0:
        return "0"
    res = ""
    while x > 0:
        res += str(x % base)
        x //= base
    return res[::-1]
