Here is the Python function to subtract two lists element-wise:

```python
def sub_list(list1, list2):
    return [a - b for a, b in zip(list1, list2)]
```

You can test this function with the provided example:

```python
print(sub_list([1, 2, 3],[4,5,6]))  # Output: [-3,-3,-3]
```

This function uses the `zip` function to pair up the elements from the two lists, and then subtracts the paired elements together. The result is a new list of the differences.
