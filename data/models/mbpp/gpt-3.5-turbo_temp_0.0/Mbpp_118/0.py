Here is the completed code snippet:

```python
def string_to_list(string):
    return string.split()

assert string_to_list("python programming") == ['python', 'programming']
```

The `split()` method is used to split a string into a list of substrings based on a specified delimiter. In this case, the delimiter is the space character. The `split()` method returns a list of the substrings, which is then returned by the `string_to_list()` function. The `assert` statement is used to verify that the function returns the expected output.