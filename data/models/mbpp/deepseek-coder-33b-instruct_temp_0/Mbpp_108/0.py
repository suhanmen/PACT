Here is the Python function to merge three lists into a single sorted list:

```python
def merge_sorted_list(list1, list2, list3):
    merged_list = list1 + list2 + list3
    merged_list.sort()
    return merged_list
```

You can test the function with the provided example:

```python
print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))
```

This should output:

```python
[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
```
