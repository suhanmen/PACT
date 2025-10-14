# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b, c, d = 1, 0, 0, 1
        while n > 0:
            if n % 2 == 1:
                a, b, c, d = (d*b + c*a), (d*(b + a) + c*b), (c*b + d*a), (d*(b + c) + c*d)
            n //= 2
            a, b, c, d = (a*a + b*c), (a*b + b*d), (c*a + d*c), (c*b + d*d)
        return b
