Here is the Python function implemented in a markdown style code block:

```python
def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count
```

You can test the function with the provided test case:

```python
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))  # Output: 3
```

This function works by iterating over each sublist in the given list. If the element is found in the sublist, the count is incremented. Finally, the function returns the count.
