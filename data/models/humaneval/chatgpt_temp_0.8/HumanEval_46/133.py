def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        prev1 = 0
        prev2 = 0
        prev3 = 0
        prev4 = 2
        for i in range(3, n+1):
            curr = prev1 + prev2 + prev3 + prev4
            prev1 = prev2
            prev2 = prev3
            prev3 = prev4
            prev4 = curr
        return curr
