def fibfib(n: int):
    cache = [0, 0, 1] + [0] * (n - 2)
    for i in range(3, n + 1):
        cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
    return cache[n-1]
