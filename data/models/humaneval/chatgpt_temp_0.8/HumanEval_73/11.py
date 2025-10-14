python
def smallest_change(arr):
    n = len(arr)
    # dp[i][j] will store the minimum number of changes needed to make the subarray arr[i:j+1] palindromic
    dp = [[0] * n for _ in range(n)]
    # base case: a subarray of length 1 is always palindromic
    for i in range(n):
        dp[i][i] = 0
    # fill the dp table diagonally
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            if arr[i] == arr[j]:
                # no change needed, the subarray is already palindromic
                dp[i][j] = dp[i+1][j-1]
            else:
                # we need to make a change, either at position i or j
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    # the minimum number of changes to make the whole array palindromic is stored in dp[0][n-1]
    return dp[0][n-1]
