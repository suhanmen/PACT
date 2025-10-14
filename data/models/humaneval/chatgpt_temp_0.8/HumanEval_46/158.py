def fib4(n: int):
    if n < 2:
        return 0
    if n == 2:
        return 2
    f = [0] * (n + 1)
    f[2] = 2
    for i in range(3, n + 1):
        f[i] = f[i-1] + f[i-2] + f[i-3] + f[i-4]
    return f[n]
