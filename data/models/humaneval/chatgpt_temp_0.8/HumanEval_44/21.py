def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    converted_num = ""
    while x > 0:
        remainder = x % base
        converted_num = str(remainder) + converted_num
        x = x // base
    return converted_num
