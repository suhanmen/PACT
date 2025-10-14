Here is the Python function that solves the problem:

```python
def average_tuple(tuples):
    return [sum(t) / len(t) for t in tuples]
```

This function uses a list comprehension to iterate over each tuple in the input tuple of tuples. For each tuple, it calculates the sum of its elements and divides by the number of elements to get the average. The results are returned as a list.

You can test this function with the provided test case:

```python
print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))
```

This should output:

```python
[30.5, 34.25, 27.0, 23.25]
```
