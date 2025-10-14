def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib_list = [0, 0, 2, 0]
        for i in range(3, n+1):
            fib_list[i%4] = fib_list[(i-1)%4] + fib_list[(i-2)%4] + fib_list[(i-3)%4] + fib_list[(i-4)%4]
        return fib_list[n%4]
