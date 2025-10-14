# CANNOT PARSE CODE SNIPPET
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x < 0:
        raise ValueError("Input number must be positive.")
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9.")
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return "".join(digits[::-1])
