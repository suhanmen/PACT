Here is the completed code snippet:

```python
def occurrence_substring(string, substring):
    if substring in string:
        start = string.index(substring)
        end = start + len(substring)
        return substring, start, end
    else:
        return None

assert occurrence_substring('python programming, python language', 'python') == ('python', 0, 6)
```

In this code, the `occurrence_substring` function takes two parameters: `string` and `substring`. It checks if the `substring` is present in the `string` using the `in` operator. If it is present, it uses the `index` method to find the starting position of the `substring` in the `string`. It then calculates the ending position by adding the length of the `substring` to the starting position. Finally, it returns a tuple containing the `substring`, starting position, and ending position.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if the function returns `('python', 0, 6)` when called with the given example inputs.