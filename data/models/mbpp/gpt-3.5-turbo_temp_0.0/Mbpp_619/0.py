Here is the completed code snippet:

```python
def move_num(string):
    letters = []
    numbers = []
    for char in string:
        if char.isdigit():
            numbers.append(char)
        else:
            letters.append(char)
    return ''.join(letters + numbers)

assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
```

In this code, we iterate through each character in the given string. If the character is a digit, we append it to the `numbers` list. Otherwise, we append it to the `letters` list. Finally, we join the `letters` and `numbers` lists together to form the desired output string.