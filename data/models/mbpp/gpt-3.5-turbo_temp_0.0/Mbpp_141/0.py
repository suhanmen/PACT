Here's the completed code snippet:

```python
def pancake_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        max_index = lst.index(max(lst[:i+1]))
        lst[:max_index+1] = lst[:max_index+1][::-1]
        lst[:i+1] = lst[:i+1][::-1]
    return lst

assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
```

The `pancake_sort` function uses a variation of the pancake sorting algorithm to sort the list. It iterates over the list from the last element to the first element. In each iteration, it finds the index of the maximum element in the unsorted portion of the list and performs two flips to move the maximum element to its correct position. Finally, it returns the sorted list.