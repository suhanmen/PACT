def smallest_change(arr):
    n = len(arr)
    # Initialize a 2D array to store the number of changes needed
    # to make the subarray arr[i:j+1] palindromic
    dp = [[0] * n for _ in range(n)]
    # Fill the diagonal of the 2D array with zeros (single-element subarrays are palindromic)
    for i in range(n):
        dp[i][i] = 0
    # Fill the upper triangle of the 2D array using dynamic programming
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j])
    # The minimum number of changes needed to make the whole array palindromic
    return dp[0][n-1]
