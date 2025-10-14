def fib4(n: int):
    fib_list = [0, 0, 2, 0]
    if n < 4:
        return fib_list[n]
    else:
        for i in range(4, n+1):
            fib_list[i % 4] = sum(fib_list)
        return fib_list[n % 4]
