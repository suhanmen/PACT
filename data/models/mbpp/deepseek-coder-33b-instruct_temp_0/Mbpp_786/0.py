Here is the Python function that solves the problem:

```python
def right_insertion(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] > value:
            return i
    return len(sorted_list)
```

This function iterates over the sorted list and checks if the current element is greater than the specified value. If it is, it returns the current index. If it doesn't find any element greater than the specified value, it returns the length of the list, which means the value should be inserted at the end of the list.
