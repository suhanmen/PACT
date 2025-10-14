def fibfib(n: int):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        f1, f2, f3 = 1, 1, 1
        for i in range(3, n+1):
            f1, f2, f3 = f2, f3, f1 + f2 + f3
        return f3 - f2 - f1
