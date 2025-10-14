# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a, b, c, d = 1, 1, 1, 0
    while n > 0:
        if n % 2 == 1:
            a, b, c, d = (a+b+c) * d, (b+d)*c + b*a, (b+d)*d + c*c, (b+c)*d
        n //= 2
        a, b, c, d = a*a + b*c, (a+b)*(b+d), (a+c)*(b+d), c*c + d*d
    return b
