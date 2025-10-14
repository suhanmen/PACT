Here is the Python function to sort the given list using the heap sort algorithm:

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
```

This function first builds a max heap from the input list, then swaps the root of the heap with the last element of the heap, reducing the size of the heap by one. The heapify function is then called to maintain the heap property. This process is repeated until the entire list is sorted.
