Here is the completed code snippet:

```python
def common_in_nested_lists(nested_lists):
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements = common_elements.intersection(lst)
    return common_elements

assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])) == set([18, 12])
```

The `common_in_nested_lists` function takes a list of nested lists as input. It initializes a set `common_elements` with the elements of the first nested list. Then, it iterates over the remaining nested lists and updates `common_elements` by taking the intersection with each nested list. Finally, it returns the set of common elements.

The `assert` statement checks if the output of `common_in_nested_lists` matches the expected set of common elements `[18, 12]`.