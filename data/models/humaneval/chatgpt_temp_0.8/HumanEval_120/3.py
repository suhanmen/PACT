import heapq

def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    # Create a min heap of size k with the first k elements of arr
    heap = arr[:k]
    heapq.heapify(heap)

    # For the remaining elements in arr, if an element is greater than the
    # smallest element in the heap, replace the smallest element with it
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])

    # Convert the heap to a list and sort it in descending order
    result = sorted(heap, reverse=True)
    return result
