# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 0 if n == 1 else 1
    else:
        a, b, c, d = 0, 0, 1, 1
        while n > 0:
            if n % 2 == 1:
                a, b, c = (d * b + c * a) % (10**9 + 7), (d * (b + a) + c * b) % (10**9 + 7), (d * b + c * a + c * b) % (10**9 + 7)
            a, b, c, d = (a * a + b * b) % (10**9 + 7), (d * b + c * a) % (10**9 + 7), (d * (b + a) + c * b) % (10**9 + 7), (d * d + c * c) % (10**9 + 7)
            n //= 2
        return b
