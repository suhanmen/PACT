Here is the completed code snippet:

```python
def check_char(string):
    if string[0] == string[-1]:
        return "Valid"
    else:
        return "Invalid"

assert check_char("abba") == "Valid"
```