# CANNOT PARSE CODE SNIPPET
def change_base(x: int, base: int) -> str:
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    digits.reverse()
    return ''.join(digits)
