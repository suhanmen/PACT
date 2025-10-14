def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        prev1, prev2, prev3 = 1, 1, 0
        for i in range(3, n+1):
            curr = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = curr
        return curr
