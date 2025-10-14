Here is the Python function that solves the problem:

```python
def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] != lst[j]:
                count += 1
    return count
```

This function works by iterating over each pair of elements in the list. If the elements are unequal, it increments a counter. The function finally returns the counter, which represents the number of unordered pairs where both elements are unequal.
