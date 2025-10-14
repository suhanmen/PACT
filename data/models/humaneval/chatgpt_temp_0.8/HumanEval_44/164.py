# CANNOT PARSE CODE SNIPPET
def change_base(x: int, base: int) -> str:
    res = ""
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res
