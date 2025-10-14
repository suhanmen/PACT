# CANNOT PARSE CODE SNIPPET
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    """
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return "".join(digits[::-1])
