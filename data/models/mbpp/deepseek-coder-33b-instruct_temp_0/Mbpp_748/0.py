Here is the Python function to put spaces between words starting with capital letters in a given string:

```python
def capital_words_spaces(s):
    return ''.join(' ' + i if i.isupper() else i for i in s).strip()
```

This function works by iterating over each character in the string. If the character is uppercase, it adds a space before it. The `strip()` function is used to remove any leading or trailing spaces.

You can test the function with the following code:

```python
print(capital_words_spaces("Python"))  # Output: 'Python'
print(capital_words_spaces("CamelCase"))  # Output: 'Camel Case'
print(capital_words_spaces("AliceInWonderland"))  # Output: 'Alice In Wonderland'
```
