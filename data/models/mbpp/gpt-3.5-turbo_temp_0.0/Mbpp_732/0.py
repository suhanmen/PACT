Here is the completed code snippet:

```python
def replace_specialchar(string):
    return string.replace(' ', ':').replace(',', ':').replace('.', ':')

assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'
```

In this code, the `replace_specialchar` function takes a string as input. It uses the `replace` method to replace all occurrences of spaces, commas, and dots with a colon. The function then returns the modified string.

The `assert` statement is used to verify that the function produces the expected output. If the output matches the expected value, the code will continue executing without any errors. Otherwise, an `AssertionError` will be raised.