def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        prev = [0, 0, 0, 2]
        for i in range(3, n+1):
            curr = prev[0] + prev[1] + prev[2] + prev[3]
            prev = prev[1:] + [curr]
        return prev[-1]
