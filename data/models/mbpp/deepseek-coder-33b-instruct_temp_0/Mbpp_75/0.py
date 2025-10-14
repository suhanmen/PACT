Here is the Python function implemented in a markdown style code block:

```python
def find_tuples(tuples_list, k):
    result = []
    for tup in tuples_list:
        if all(num % k == 0 for num in tup):
            result.append(tup)
    return result
```

This function works by iterating over each tuple in the input list. For each tuple, it checks if all elements are divisible by `k` using the `all()` function and a generator expression. If all elements are divisible, the tuple is added to the result list. Finally, the function returns the result list.
