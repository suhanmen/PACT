Here is the Python function that solves the problem:

```python
def merge(lst):
    return [[sublist[i] for sublist in lst] for i in range(2)]
```

This function uses list comprehension to create a new list of lists. The outer list comprehension iterates over the indices 0 and 1 (which represent the two elements in each sublist). The inner list comprehension then iterates over each sublist in the input list, and adds the element at the current index to the new list.

You can test this function with the provided test case:

```python
print(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]))  # Output: [['x', 'a', 'm'], ['y', 'b', 'n']]
```
