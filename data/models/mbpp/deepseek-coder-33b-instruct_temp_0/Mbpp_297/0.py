Here is the Python function to flatten a given nested list structure:

```python
def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list
```

This function uses recursion to flatten the nested list. It checks if each element in the list is a list itself. If it is, it calls the function again on that list. If it's not, it appends the element to the `flat_list`. The `extend` method is used to add all elements of the nested list to the `flat_list`.

You can test the function with the provided example:

```python
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
```

This should output:

```python
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
```
