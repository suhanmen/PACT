def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x < 0 or base < 2 or base > 9:
        return "Invalid input"
    
    result = ""
    while x != 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    
    return result
