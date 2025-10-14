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
    memo = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                memo[i][j] = memo[i+1][j-1]
            else:
                memo[i][j] = min(memo[i+1][j], memo[i][j-1]) + 1
    return memo[0][n-1]
