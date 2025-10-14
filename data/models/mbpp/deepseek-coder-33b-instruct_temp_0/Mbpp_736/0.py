Here is the Python function to locate the left insertion point for a specified value in sorted order:

```python
def left_insertion(sorted_list, value):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= value:
            return i
    return len(sorted_list)
```

This function iterates over the sorted list and checks if the current element is greater than or equal to the specified value. If it is, it returns the current index. If no such element is found, it returns the length of the list, which is the index where the value would be inserted to keep the list sorted.
