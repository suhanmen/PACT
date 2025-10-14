# CANNOT PARSE CODE SNIPPET
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    # Handle the case where x is 0
    if x == 0:
        return '0'
    
    # Initialize variables
    result = ''
    
    # Convert to the new base
    while x > 0:
        digit = x % base
        result = str(digit) + result
        x //= base

    return result
