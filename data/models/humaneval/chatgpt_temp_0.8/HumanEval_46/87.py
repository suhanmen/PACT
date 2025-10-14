def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib1, fib2, fib3, fib4 = 0, 0, 2, 0
        for i in range(3, n+1):
            fib4 = fib1 + fib2 + fib3 + fib4
            fib1, fib2, fib3 = fib2, fib3, fib4
        return fib4
