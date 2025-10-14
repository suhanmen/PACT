def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9.")

    digits = []
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x //= base

    return "".join(digits[::-1])
