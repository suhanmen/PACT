# CANNOT PARSE CODE SNIPPET
python
def fibfib(n: int) -> int:
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    fib1, fib2, fib3 = 0, 0, 1
    for i in range(3, n+1):
        fib1, fib2, fib3 = fib2, fib3, fib1 + fib2 + fib3
    return fib3
