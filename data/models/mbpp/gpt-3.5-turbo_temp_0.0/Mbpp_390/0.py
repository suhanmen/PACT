Here is the completed code snippet:

```python
def add_string(lst, format_string):
    return [format_string.format(element) for element in lst]

assert add_string([1,2,3,4],'temp{0}') == ['temp1', 'temp2', 'temp3', 'temp4']
```

In this code, the `add_string` function takes two parameters: `lst`, which is the list of elements, and `format_string`, which is the format string to be applied to each element. The function uses a list comprehension to iterate over each element in the list and apply the format string using the `format` method. The resulting formatted strings are then returned as a new list. The `assert` statement is used to verify that the function produces the expected output.