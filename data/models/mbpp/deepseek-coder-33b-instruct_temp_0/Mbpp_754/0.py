Here is the Python function to solve the problem:

```python
def extract_index_list(l1, l2, l3):
    common_elements = []
    for i in range(min(len(l1), len(l2), len(l3))):
        if l1[i] == l2[i] == l3[i]:
            common_elements.append(l1[i])
    return common_elements
```

This function works by iterating over the indices of the shortest list (`l1`, `l2`, or `l3`). For each index, it checks if the elements at that index in `l1`, `l2`, and `l3` are all equal. If they are, it adds that element to the `common_elements` list. Finally, it returns the `common_elements` list.

You can test this function with the provided test case:

```python
print(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))  # Output: [1, 7]
```

This should return `[1, 7]`, which is the expected output.
