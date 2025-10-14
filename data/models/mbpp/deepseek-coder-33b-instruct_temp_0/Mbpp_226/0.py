Here is the Python function to remove the characters which have odd index values of a given string:

```python
def odd_values_string(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i]
    return result
```

You can test the function with the following code:

```python
print(odd_values_string('abcdef'))  # Output: 'ace'
```

This function works by iterating over the string and adding the characters at even index positions to the result string. The `%` operator is used to check if the index is even. If the index is even, the character is added to the result string.
