Here is the Python function that moves all the numbers to the end of the given string:

```python
def move_num(s):
    nums = []
    letters = []
    for char in s:
        if char.isdigit():
            nums.append(char)
        else:
            letters.append(char)
    return ''.join(letters + nums)

print(move_num('I1love143you55three3000thousand'))
```

This function works by iterating over each character in the string. If the character is a digit, it is added to the `nums` list. If it is a letter, it is added to the `letters` list. Finally, the function returns a string that is the concatenation of the `letters` list and the `nums` list.

The `isdigit()` function is used to check if a character is a digit. If the character is a digit, `isdigit()` returns `True`, otherwise it returns `False`.

The `join()` function is used to concatenate the elements of the `letters` and `nums` lists into a single string. The `+` operator is used to concatenate the two lists.
