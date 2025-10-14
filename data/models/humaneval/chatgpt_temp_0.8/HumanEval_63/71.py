def fibfib(n: int):
    fibs = [0, 0, 1]
    if n < 3:
        return fibs[n-1]
    for i in range(3, n+1):
        fibs[i%3] = fibs[(i-1)%3] + fibs[(i-2)%3] + fibs[(i-3)%3]
    return fibs[n%3]
