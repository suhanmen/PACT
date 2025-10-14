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
    # create a dp table with n rows and n columns
    dp = [[0 for x in range(n)] for y in range(n)]
    # fill the dp table diagonally
    for i in range(n):
        dp[i][i] = 0
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if arr[i] == arr[j] and cl == 2:
                dp[i][j] = 0
            elif arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j])
    return dp[0][n-1]
