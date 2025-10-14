def fibfib(n: int):
    memo = [0, 0, 1] # memoization
    if n < 3:
        return memo[n]
    for i in range(3, n+1):
        memo.append(memo[i-1] + memo[i-2] + memo[i-3])
    return memo[n]
