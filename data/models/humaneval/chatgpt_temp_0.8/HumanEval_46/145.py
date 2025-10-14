def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        fib0, fib1, fib2, fib3 = 0, 0, 2, 0
        for i in range(3, n+1):
            fib3, fib2, fib1, fib0 = fib2, fib1, fib0, fib3 + fib2 + fib1 + fib0
        return fib3 + fib2 + fib1 + fib0
