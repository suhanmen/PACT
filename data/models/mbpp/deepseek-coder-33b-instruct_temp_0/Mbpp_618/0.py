Here is the Python function to divide two lists element wise:

```python
def div_list(list1, list2):
    return [float(a)/b for a, b in zip(list1, list2)]
```

You can test this function with the provided example:

```python
print(div_list([4,5,6],[1, 2, 3]))  # Output: [4.0,2.5,2.0]
```

This function uses list comprehension and the `zip` function to iterate over the two lists simultaneously. It divides the corresponding elements from each list and returns the result as a new list. The `float` function is used to ensure that the result is a floating point number, even if the division results in an integer.
