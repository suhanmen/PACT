def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if base == 10:
        return str(x)
    elif x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)
