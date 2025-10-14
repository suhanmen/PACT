Here is the completed code snippet:

```python
def remove_parenthesis(string):
    start = string.find("(")
    end = string.find(")")
    if start != -1 and end != -1:
        return string[:start] + string[end+1:]
    else:
        return string

assert remove_parenthesis("python (chrome)") == "python"
```

This function finds the indices of the opening and closing parentheses in the string using the `find()` method. If both indices are found, it returns the string with the content between the parentheses removed. If either index is not found, it returns the original string.