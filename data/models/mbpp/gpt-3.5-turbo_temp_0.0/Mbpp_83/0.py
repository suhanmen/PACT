Here is the completed code snippet:

```python
def get_Char(string):
    total = 0
    for char in string:
        total += ord(char)
    return chr((total % 26) + 97)

assert get_Char("abc") == "f"
```

In this code, the `get_Char` function takes a string as input. It iterates over each character in the string and adds the ASCII value of each character to the `total` variable. Then, it calculates the modulo 26 of the `total` and adds 97 to get the ASCII value of the resulting character. Finally, it converts the ASCII value back to a character using the `chr` function and returns the character.