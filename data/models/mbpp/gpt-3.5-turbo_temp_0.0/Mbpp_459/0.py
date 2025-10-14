Here is the completed code snippet:

```python
def remove_uppercase(string):
    return ''.join(char for char in string if not char.isupper())

assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
```

In this code, the `remove_uppercase` function takes a string as input. It uses a list comprehension to iterate over each character in the string. If the character is not uppercase (determined using the `isupper()` method), it is added to a new list. Finally, the function returns the joined string of the characters in the new list.

The `assert` statement is used to verify that the function produces the expected output.