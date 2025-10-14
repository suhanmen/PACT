Here is the completed code snippet:

```python
def toggle_string(string):
    toggled_string = ""
    for char in string:
        if char.islower():
            toggled_string += char.upper()
        else:
            toggled_string += char.lower()
    return toggled_string

assert toggle_string("Python") == "pYTHON"
```

The `toggle_string` function takes a string as input and iterates through each character. If the character is lowercase, it converts it to uppercase and appends it to the `toggled_string`. If the character is uppercase, it converts it to lowercase and appends it to the `toggled_string`. Finally, it returns the `toggled_string`.