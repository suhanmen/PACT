def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib_nums = [0, 0, 2, 0]
        for i in range(4, n+1):
            fib_nums[i%4] = fib_nums[(i-1)%4] + fib_nums[(i-2)%4] + fib_nums[(i-3)%4] + fib_nums[(i-4)%4]
        return fib_nums[n%4]
