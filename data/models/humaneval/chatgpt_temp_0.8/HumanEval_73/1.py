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
    dp = [[0] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if arr[i] == arr[j]:
                dp[j][i] = dp[j+1][i-1]
            else:
                dp[j][i] = 1 + min(dp[j+1][i], dp[j][i-1])
    return dp[0][n-1]
