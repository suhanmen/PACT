Here is the Python function to find the tuple intersection of elements in the given tuple list irrespective of their order:

```python
def tuple_intersection(t1, t2):
    # Convert each tuple to a set of tuples
    set1 = set(map(tuple, map(sorted, t1)))
    set2 = set(map(tuple, map(sorted, t2)))

    # Find the intersection of the two sets
    intersection = set1 & set2

    # Convert the result back to a list of tuples
    result = list(map(tuple, intersection))

    return result
```

This function works by first converting each tuple in the list to a set of tuples. This is done by using the `map` function to apply the `sorted` function to each tuple in the list, which sorts the elements of the tuple. The `sorted` function returns a list, so we need to convert it back to a tuple using the `tuple` function.

Then, we find the intersection of the two sets using the `&` operator. The intersection of two sets is a set that contains only the elements that are in both sets.

Finally, we convert the result back to a list of tuples using the `map` function.

You can test this function with the provided test case:

```python
print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]))
```

This should output:

```python
[(4, 5), (3, 4), (5, 6)]
```
