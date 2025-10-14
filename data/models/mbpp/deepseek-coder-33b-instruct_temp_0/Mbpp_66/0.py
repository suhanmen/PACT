Here is the Python function implemented in a markdown style code block:

```python
def pos_count(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    return count
```

You can test the function with the following code:

```python
assert pos_count([1,-2,3,-4]) == 2
```
