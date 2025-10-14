Here is the Python function to solve the problem:

```python
def union_elements(t1, t2):
    # Combine the two tuples
    combined = t1 + t2
    # Convert the combined tuple to a set to remove duplicates
    unique_elements = set(combined)
    # Convert the set back to a tuple and sort it
    sorted_tuple = tuple(sorted(unique_elements))
    return sorted_tuple
```

You can test the function with the provided example:

```python
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
```

This should output:

```python
(3, 4, 5, 6, 7, 10)
```
