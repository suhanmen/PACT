"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""



def odd_length_sum(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n, 2):
            total_sum += sum(arr[i:j+1])
    return total_sum

# Example usage
# assert odd_length_sum([1,2,4]) == 14
