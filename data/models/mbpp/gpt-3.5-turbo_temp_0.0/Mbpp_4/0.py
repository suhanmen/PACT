Here is the completed code snippet:

```python
import heapq

def heap_queue_largest(numbers, n):
    return heapq.nlargest(n, numbers)

assert heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
```

In this code, we use the `heapq.nlargest()` function from the `heapq` module to find the `n` largest integers from the given list of numbers. The function returns a new list containing the `n` largest integers in descending order. We then use an `assert` statement to verify that the function returns the expected result.