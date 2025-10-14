Here is the Python function to find the intersection of two arrays:

```python
def intersection_array(arr1, arr2):
    return list(set(arr1) & set(arr2))
```

This function works by converting the input arrays to sets, which automatically remove any duplicate values. The `&` operator is then used to find the intersection of the two sets, which gives us the common elements in both arrays. Finally, the result is converted back to a list.

You can test this function with the provided example:

```python
print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]))
```

This should output:

```python
[1, 2, 8, 9]
```
