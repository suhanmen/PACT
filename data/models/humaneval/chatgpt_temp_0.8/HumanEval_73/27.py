def smallest_change(arr):
    n = len(arr)
    memo = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        memo[i][i+1] = 1 if arr[i] != arr[i+1] else 0
    for i in range(2, n):
        for j in range(n - i):
            if arr[j] == arr[j+i]:
                memo[j][j+i] = memo[j+1][j+i-1]
            else:
                memo[j][j+i] = 1 + min(memo[j+1][j+i], memo[j][j+i-1])
    return memo[0][n-1]
