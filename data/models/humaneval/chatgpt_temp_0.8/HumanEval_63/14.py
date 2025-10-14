def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    prev1, prev2, prev3 = 1, 0, 0
    for i in range(3, n+1):
        current = prev1 + prev2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = current
    return current
