python
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
    # We can solve this problem by finding the longest common subsequence
    # between the array and its reverse. The number of elements that need
    # to be changed is equal to the difference between the length of the
    # array and the length of its longest common subsequence with its reverse.
    n = len(arr)
    rev_arr = arr[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i - 1] == rev_arr[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
         
