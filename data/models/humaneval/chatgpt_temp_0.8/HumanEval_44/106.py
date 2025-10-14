def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    output = ""
    while x:
        output = str(x % base) + output
        x //= base
    return output
