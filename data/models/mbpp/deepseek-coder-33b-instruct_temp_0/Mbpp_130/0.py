Here is the Python function to find the item with maximum frequency in a given list:

```python
def max_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    max_count = max(count_dict.values())
    max_items = [item for item, count in count_dict.items() if count == max_count]
    return max_items
```

This function first creates a dictionary where the keys are the items in the list and the values are the counts of those items. It then finds the maximum count and returns a list of items that have this maximum count.

Please note that if there are multiple items with the same maximum frequency, this function will return all of them. If you want only one of them, you can modify the function to return the first item in the list of maximum items.
