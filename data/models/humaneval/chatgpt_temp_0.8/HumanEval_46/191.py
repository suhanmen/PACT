# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib_1 = 0
        fib_2 = 0
        fib_3 = 0
        fib_4 = 2
        for i in range(3, n+1):
            fib_n = fib_1 + fib_2 + fib_3 + fib_4
            fib_1 = fib_2
            fib_2 = fib_3
            fib_3 = fib_4
            fib_4 = fib_n
        return fib_n
