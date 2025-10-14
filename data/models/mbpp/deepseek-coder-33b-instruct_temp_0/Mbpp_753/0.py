Here is the Python function to find minimum k records from tuple list:

```python
def min_k(tuples, k):
    # Sort the list of tuples based on the second element of each tuple
    tuples.sort(key=lambda x: x[1])
    
    # Return the first k elements of the sorted list
    return tuples[:k]
```

You can test this function with the following code:

```python
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
```

This function works by first sorting the list of tuples based on the second element of each tuple (i.e., the number). It then returns the first k elements of the sorted list.
