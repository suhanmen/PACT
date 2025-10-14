Here is the completed code snippet:

```python
def text_match_two_three(string):
    if 'abb' in string or 'abbb' in string:
        return True
    else:
        return False

assert text_match_two_three("ac") == False
```

This function checks whether the string contains the sequence 'abb' or 'abbb'. If either of these sequences is found in the string, the function returns True. Otherwise, it returns False. The assert statement at the end verifies that the function behaves as expected for the given example.