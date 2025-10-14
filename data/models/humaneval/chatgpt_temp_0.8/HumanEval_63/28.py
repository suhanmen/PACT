def fibfib(n: int):
    fib = [0, 0, 1] # initialize the first 3 values
    if n < 3:
        return fib[n]
    for i in range(3, n+1):
        fib.append(fib[i-1] + fib[i-2] + fib[i-3])
    return fib[n]
