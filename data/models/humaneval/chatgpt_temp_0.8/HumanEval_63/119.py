# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c, d = 1, 1, 1, 0
        n -= 2
        while n > 0:
            if n % 2 == 1:
                a, b, c, d = (a + b + c) * d, a * d + b * c, b * d + a * c, b * c + c * d + d * d
            n //= 2
            a, b, c, d = a * a + b * b + c * c, b * (a + d), c * (a + d), d * d + b * c
        return a + b + c
