Here is the completed code snippet:

```python
def merge_sorted_list(list1, list2, list3):
    merged_list = list1 + list2 + list3
    merged_list.sort()
    return merged_list

assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
```

The `merge_sorted_list` function takes three lists as input and merges them into a single list using the `+` operator. Then, the `sort` method is used to sort the merged list in ascending order. Finally, the sorted merged list is returned.

The `assert` statement is used to verify that the function produces the expected output.