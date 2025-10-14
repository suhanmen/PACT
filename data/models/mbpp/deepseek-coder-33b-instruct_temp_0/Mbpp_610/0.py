Here is the Python function that removes the k'th element from a list:

```python
def remove_kth_element(input_list, k):
    if k < len(input_list):
        del input_list[k]
    return input_list
```

You can test this function with the provided example:

```python
print(remove_kth_element([1,1,2,3,4,4,5,1], 3))  # Output: [1, 1, 2, 4, 4, 5, 1]
```

Please note that Python uses zero-based indexing, so the third element is at index 2.
