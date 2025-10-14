"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""


import bisect

def max_sum_increasing_subseq(arr, n, i, k):
    # Initialize DP array
    dp = [0] * n
    dp[0] = arr[0]

    # Fill dp array with maximum sum values
    for j in range(1, n):
        for m in range(j):
            if arr[m] < arr[j]:
                dp[j] = max(dp[j], dp[m] + arr[j])
            else:
                dp[j] = max(dp[j], arr[j])

    # Include the kth element in the sum
    max_sum_with_k = dp[i] + arr[k]

    # Find the maximum sum until the ith index
    max_sum_until_i = max(dp[:i+1])

    # The result is the max of the sum until i or the sum with k
    result = max(max_sum_until_i, max_sum_with_k)
    return result

# Example usage
# assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
