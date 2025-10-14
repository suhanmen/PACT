def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        f0, f1, f2, f3 = 0, 0, 2, 0
        for i in range(3, n+1):
            f3 = f0 + f1 + f2 + f3
            f0, f1, f2 = f1, f2, f3
        return f3
