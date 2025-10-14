Here is the completed code snippet:

```python
def extract_singly(list_of_lists):
    flattened_list = []
    for sublist in list_of_lists:
        flattened_list.extend(sublist)
    return flattened_list
```

This function takes a list of lists as input and returns a single list containing all the elements from the input lists. The `extend()` method is used to add the elements from each sublist to the `flattened_list`. Finally, the function returns the `flattened_list`.

The `assert` statement checks if the output of the function matches the expected output, which is a set containing the numbers [3, 4, 5, 7, 1].