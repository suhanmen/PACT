Here is the completed code snippet:

```python
def min_k(records, k):
    sorted_records = sorted(records, key=lambda x: x[1])
    return sorted_records[:k]

# test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
```