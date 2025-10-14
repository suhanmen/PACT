Here is the completed code snippet:

```python
def count_list(lists):
    count = 0
    for item in lists:
        if isinstance(item, list):
            count += 1
    return count

assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
```