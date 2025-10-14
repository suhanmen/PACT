# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    fib0, fib1, fib2, fib3 = 0, 0, 1, 1
    for i in range(3, n+1):
        fib0, fib1, fib2, fib3 = fib1, fib2, fib3, fib1+fib2+fib3
    return fib0 if n <= 1 else fib3
