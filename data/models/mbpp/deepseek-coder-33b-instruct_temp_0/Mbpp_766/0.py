Here is the Python function implemented in a markdown style code block:

```python
def pair_wise(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]
```

This function uses list comprehension to generate a list of tuples, where each tuple is a pair of consecutive items in the input list. The range function is used to iterate over the indices of the list, and for each index, the function creates a tuple containing the item at that index and the item at the next index.

You can test this function with the provided test case:

```python
print(pair_wise([1,1,2,3,3,4,4,5]))
```

This should output:

```python
[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
```
