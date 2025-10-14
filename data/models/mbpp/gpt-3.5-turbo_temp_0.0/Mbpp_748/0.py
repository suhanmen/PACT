Here is the completed code snippet:

```python
def capital_words_spaces(string):
    result = ""
    for i in range(len(string)):
        if i > 0 and string[i].isupper():
            result += " "
        result += string[i]
    return result
```

This function takes a string as input and iterates through each character. If the character is uppercase and not the first character in the string, a space is added before it. The resulting string is then returned.