def smallest_change(arr):
    n = len(arr)
    # Initialize a 2D table to store the minimum number of changes for each subarray
    dp = [[0] * n for _ in range(n)]
    # Fill the table diagonally with 0's (a subarray of length 1 is already palindromic)
    for i in range(n):
        dp[i][i] = 0
    # Fill the table bottom-up, starting with subarrays of length 2
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            # If the first and last elements are equal, no change is needed
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            # Otherwise, try changing either the first or last element
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    # The minimum number of changes for the whole array is stored in dp[0][n-1]
    return dp[0][n-1]
