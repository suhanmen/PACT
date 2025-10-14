Here is the Python function that solves the problem:

```python
def add_string(lst, fmt):
    return [fmt.format(i) for i in lst]
```

This function uses a list comprehension to iterate over each element in the input list `lst`. For each element, it applies the `format` method to the format string `fmt`, replacing `{0}` with the current element. The results are collected into a new list which is returned by the function.

You can test the function with the provided test case:

```python
print(add_string([1,2,3,4],'temp{0}'))  # Output: ['temp1', 'temp2', 'temp3', 'temp4']
```
