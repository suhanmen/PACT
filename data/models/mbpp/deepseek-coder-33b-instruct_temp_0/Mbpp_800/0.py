Here is the Python function to remove all whitespaces from a string:

```python
def remove_all_spaces(input_string):
    return input_string.replace(" ", "")
```

You can test the function with the following code:

```python
assert remove_all_spaces('python  program')==('pythonprogram')
```

This function works by using the `replace` method of the string class in Python, which replaces all occurrences of a specified character (in this case, a space) with another character (in this case, no character, effectively removing it).
