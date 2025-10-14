Here is the Python function implemented in a markdown style code block:

```python
def sum_even_and_even_index(lst):
    return sum(value for index, value in enumerate(lst) if index % 2 == 0 and value % 2 == 0)

# Test the function
print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))  # Output: 30
```

This function uses a generator expression inside the `sum` function to iterate over the list `lst` and select only the elements that are at an even index (`index % 2 == 0`) and are even themselves (`value % 2 == 0`). The `enumerate` function is used to get both the index and the value of each element in the list.
