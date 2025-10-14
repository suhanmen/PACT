Here is the completed code snippet:

```python
def extract_index_list(l1, l2, l3):
    common_elements = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            common_elements.append(l1[i])
    return common_elements

assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
```

The `extract_index_list` function takes three lists as input (`l1`, `l2`, `l3`) and initializes an empty list `common_elements` to store the common elements. It then iterates over the indices of the lists using a for loop. If the element at the current index is the same in all three lists, it is appended to the `common_elements` list. Finally, the function returns the `common_elements` list.

The provided assert statement checks if the function correctly finds the common elements `[1, 7]` from the given lists and returns it.