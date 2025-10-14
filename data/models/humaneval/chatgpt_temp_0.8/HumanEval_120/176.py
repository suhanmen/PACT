import heapq

def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    # Use a min heap to keep track of the k largest elements seen so far
    heap = []
    for x in arr:
        if len(heap) < k:
            heapq.heappush(heap, x)
        else:
            heapq.heappushpop(heap, x)
    # Sort the result in decreasing order
    return sorted(heap, reverse=True)
