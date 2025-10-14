Here is the Python function to remove uppercase substrings from a given string:

```python
def remove_uppercase(s):
    return ''.join([i for i in s if not i.isupper()])

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
```

This function works by iterating over each character in the string `s` and checking if it is uppercase using the `isupper()` method. If the character is not uppercase, it is added to the result string. The `join()` method is used to concatenate all the characters in the result string into a single string.

When you run this function with the input 'cAstyoUrFavoRitETVshoWs', it will return 'cstyoravoitshos', which is the string with all uppercase characters removed.
