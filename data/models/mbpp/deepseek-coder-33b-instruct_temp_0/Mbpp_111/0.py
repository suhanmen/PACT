Here is the Python function to find the common elements in given nested lists:

```python
def common_in_nested_lists(nested_lists):
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements &= set(lst)
    return list(common_elements)
```

You can test the function with the provided example:

```python
print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])))
```

This should output:

```python
{18, 12}
```

This function works by first converting the first list to a set and then intersecting it with the sets of the remaining lists. The intersection operation (`&=`) keeps only the elements that are common to all sets. The result is a set of common elements, which is then converted back to a list.
