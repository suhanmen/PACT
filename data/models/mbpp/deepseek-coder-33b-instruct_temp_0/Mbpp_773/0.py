Here is the Python function that solves the problem:

```python
def occurrence_substring(string, substring):
    index = string.find(substring)
    if index != -1:
        return (substring, index, index + len(substring) - 1)
    else:
        return None

print(occurrence_substring('python programming, python language','python'))
```

This function uses the `find` method of the string class to find the first occurrence of the substring in the string. If the substring is found, it returns a tuple containing the substring, the start index, and the end index of the substring. If the substring is not found, it returns `None`.
