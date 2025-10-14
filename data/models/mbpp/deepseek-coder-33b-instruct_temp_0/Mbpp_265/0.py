Here is the Python function implemented in a markdown style code block:

```python
def list_split(lst, n):
    return [lst[i::n] for i in range(n)]
```

This function uses list comprehension to create a new list of lists. The `range(n)` generates indices from 0 to n-1. For each index `i`, it creates a new list that starts at index `i` and takes every `n`th element.

You can test this function with the provided test case:

```python
print(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3))
```

This should output:

```python
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
```
