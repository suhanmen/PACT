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
    if len(arr) == 0:
        return 0
    
    # Create a copy of the input array
    arr_copy = arr[:]
    
    # Reverse the copy of the array
    arr_copy.reverse()
    
    # Compute the length of the longest common subsequence between the original
    # array and the reversed copy of the array
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i - 1] == arr_copy[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs_length = dp[n][n]
    
    # The answer is the difference between the length of the input array and
    # the length of the longest common subsequence
    return n - lcs_length
