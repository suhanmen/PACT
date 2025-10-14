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
    # Initialize a 2D array of size n x n to keep track of the minimum number of changes required
    # to make the subarray from i to j (inclusive) palindromic.
    dp = [[0] * n for _ in range(n)]
    # Fill in the diagonal of the 2D array with 0s (a single element is already palindromic)
    for i in range(n):
        dp[i][i] = 0
    # Fill in the rest of the 2D array by considering all possible subarrays of increasing length
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    # The minimum number of changes required to make the whole array palindromic is stored at dp[0][n-1]
    return dp[0][n-1]
