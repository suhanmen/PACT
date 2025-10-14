# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib1 = 0
        fib2 = 1
        fib3 = 1
        for i in range(3, n+1):
            fib = fib1 + fib2 + fib3
            fib1 = fib2
            fib2 = fib3
            fib3 = fib
        return fib3
