def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    n = len(arr)
    # Initialize a 2D array of size n x n with 0's
    dp = [[0 for i in range(n)] for j in range(n)]
    # Iterate over all subarrays of length 2 and fill the dp array
    for i in range(n - 1):
        if arr[i] == arr[i+1]:
            dp[i][i+1] = 0
        else:
            dp[i][i+1] = 1
    # Iterate over all subarrays of length greater than 2 and fill the dp array
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j])
    # Return the minimum number of changes required for the entire array
    return dp[0][n-1]
