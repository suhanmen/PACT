import heapq

def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # We use a min heap to keep track of k maximum elements
    heap = []
    
    # Iterate over the array and push the first k elements onto the heap
    for i in range(k):
        heapq.heappush(heap, arr[i])
    
    # For the remaining elements in the array, we check if they are larger than the 
    # smallest element in the heap. If they are, we replace the smallest element in 
    # the heap with t
