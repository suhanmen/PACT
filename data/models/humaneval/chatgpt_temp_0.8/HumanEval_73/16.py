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

    # initialize variables
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # base case
    for i in range(n):
        dp[i][i] = 1

    # fill in table diagonally
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if arr[i] == arr[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # return number of changes needed
    return n - dp[0][n-1]
