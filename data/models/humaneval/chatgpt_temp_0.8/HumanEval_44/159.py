def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("Base should be between 2 and 9")
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result
