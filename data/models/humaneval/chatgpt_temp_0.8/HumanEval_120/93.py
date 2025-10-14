import heapq

def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    # use a min heap to keep track of the k largest numbers seen so far
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
    # convert the heap to a sorted list and return it
    return sorted(heap, reverse=True)
