def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    quotient = x
    result = ""
    while quotient > 0:
        remainder = quotient % base
        quotient = quotient // base
        result = str(remainder) + result
    return result
