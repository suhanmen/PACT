Here is the completed code snippet:

```python
def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)

assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
```

The `sequential_search` function takes in an array (`arr`) and an element (`element`). It iterates through each element in the array and checks if it is equal to the given element. If a match is found, it returns a tuple `(True, i)` where `i` is the index position of the element. If no match is found, it returns `(False, -1)` indicating that the element is not in the array.