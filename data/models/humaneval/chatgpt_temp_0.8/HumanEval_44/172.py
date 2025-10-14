def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    digits = "0123456789"
    if x < base:
        return digits[x]
    else:
        return change_base(x//base, base) + digits[x % base]
