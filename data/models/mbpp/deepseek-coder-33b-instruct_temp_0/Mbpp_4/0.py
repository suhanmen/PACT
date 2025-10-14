Here is the Python function implemented in a markdown style code block:

```python
def heap_queue_largest(nums, n):
    import heapq
    return heapq.nlargest(n, nums)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))
```

This function uses the `heapq.nlargest` function from Python's `heapq` module to find the `n` largest numbers in the list. The `heapq.nlargest` function returns the `n` largest elements from the iterable specified and it internally uses a heap data structure.

The `heapq.nlargest` function returns the elements in descending order.

Please note that the `heapq.nlargest` function returns the `n` largest elements in descending order. If you want the elements in ascending order, you can use the `heapq.nsmallest` function.
