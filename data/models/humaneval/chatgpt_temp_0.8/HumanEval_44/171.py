# CANNOT PARSE CODE SNIPPET
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10."""
    if x < 0 or base < 2 or base > 9:
        return None
    if x == 0:
        return '0'
    result = ''
    while x > 0:
        digit = x % base
        result = str(digit) + result
        x = x // base
    return result
