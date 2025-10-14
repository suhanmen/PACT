"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""


import numpy as np

def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Initialize max_product array to store the maximum product till ith element
    max_product_array = np.ones(n)

    # Fill max_product_array[] in bottom-up manner
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                max_product_array[i] = max(max_product_array[i], max_product_array[j] * arr[i])

    # Return the maximum value from max_product_array[]
    return int(max(max_product_array))

# Example usage
# assert max_product([3, 100, 4, 5, 150, 6]) == 3000
