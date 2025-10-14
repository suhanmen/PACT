def smallest_change(arr):
    n = len(arr)
    # Initialize a 2D table to store the minimum number of changes needed 
    # to make a subarray arr[i:j+1] palindromic.
    dp = [[0] * n for _ in range(n)]
    # Fill in the base cases for subarrays of length 1.
    for i in range(n):
        dp[i][i] = 0
    # Fill in the base cases for subarrays of length 2.
    for i in range(n - 1):
        dp[i][i+1] = 0 if arr[i] == arr[i+1] else 1
    # Fill in the rest of the table using dynamic programming.
    for l in range(3, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
            if arr[i] == arr[j]:
                dp[i][j] = min(dp[i][j], dp[i+1][j-1])
    # The minimum number of changes needed to make the whole array palindromic
    # is the same as the minimum number of changes needed to make the subarray
    # arr[0:n-1] palindromic.
    return dp[0][n-1]
