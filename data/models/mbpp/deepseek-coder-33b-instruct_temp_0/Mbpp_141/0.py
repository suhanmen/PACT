Here is the Python function to sort a list of elements using the Pancake Sort algorithm:

```python
def pancake_sort(lst):
    def flip(arr, i):
        start = 0
        while start < i:
            temp = arr[start]
            arr[start] = arr[i]
            arr[i] = temp
            start += 1
            i -= 1

    n = len(lst)
    for curr_size in reversed(range(2, n+1)):
        max_index = lst.index(max(lst[:curr_size]))
        if max_index != curr_size - 1:
            flip(lst, max_index)
            flip(lst, curr_size - 1)
    return lst

print(pancake_sort([15, 79, 25, 38, 69]))  # Output: [15, 25, 38, 69, 79]
```

This function works by repeatedly finding the maximum element in the unsorted part of the list and moving it to the end of the list. It does this by flipping the list at the index of the maximum element and then flipping the entire list. This process is repeated for the remaining unsorted part of the list.
