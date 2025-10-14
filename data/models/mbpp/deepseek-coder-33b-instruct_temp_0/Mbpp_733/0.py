Here is the Python function to find the index of the first occurrence of a given number in a sorted array:

```python
def find_first_occurrence(arr, num):
    try:
        return arr.index(num)
    except ValueError:
        return -1
```

This function uses the built-in `index` method of Python lists, which returns the index of the first occurrence of a given element in the list. If the element is not found, it raises a `ValueError`, which we catch and return `-1` in this case.

You can test this function with the provided test case:

```python
print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # Output: 1
```

This will output `1`, which is the index of the first occurrence of `5` in the array.
