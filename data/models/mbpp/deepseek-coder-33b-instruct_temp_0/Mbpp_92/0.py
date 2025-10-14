Here is the Python function to check whether the given number is undulating or not:

```python
def is_undulating(n):
    n = str(n)
    if len(n) < 3:
        return False
    else:
        for i in range(2, len(n)):
            if n[i] != n[i-2]:
                return False
        return True
```

This function works by converting the number to a string, then checking if the third character from the start is the same as the first character from the start. If it is not, the function returns False. If it is, the function continues to check the rest of the string, returning False if it finds a character that is not the same as the character two positions before. If it gets through the entire string without finding any such characters, the function returns True.
