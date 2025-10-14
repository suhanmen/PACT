# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        fib1, fib2, fib3 = 1, 1, 0
        for i in range(3, n+1):
            fib3, fib2, fib1 = fib2 + fib3 + fib1, fib3, fib2
        return fib3
