# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 1
    a, b, c, d, e = 0, 0, 1, 1, 1
    while n > 0:
        if n % 2 == 1:
            a, b, c, d, e = (a + b + c), a, b, c, (d + e)
        n //= 2
        a, b, c, d, e = (a**2 + b*c), (a*b + b*d), (a*c + c*e), (b*c + d*e), (c**2 + e**2)
    return b
