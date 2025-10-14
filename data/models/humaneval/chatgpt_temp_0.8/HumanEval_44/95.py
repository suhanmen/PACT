def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    """
    assert 2 <= base <= 9, "Base must be between 2 and 9"
    if x == 0:
        return '0'
    digits = []
    while x > 0:
        digit = x % base
        digits.append(str(digit))
        x //= base
    digits.reverse()
    return ''.join(digits)
