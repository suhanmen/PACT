Here is the Python function that solves the problem:

```python
def count_same_pair(list1, list2):
    return sum(1 for a, b in zip(list1, list2) if a == b)
```

This function uses the `zip` function to pair up the elements from the two lists. It then uses a generator expression to count the number of pairs where the elements are equal. The `sum` function adds up these counts.

You can test this function with the provided example:

```python
print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))  # Output: 4
```
