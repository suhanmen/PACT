Here is the completed code snippet:

```python
def count_char_position(string):
    count = 0
    for i, char in enumerate(string):
        if char.lower() == chr(ord('a') + i):
            count += 1
    return count

assert count_char_position("xbcefg") == 2
```

In this code, we define a function `count_char_position` that takes a string as input. We initialize a variable `count` to keep track of the number of characters that occur at the same position in the string as in the English alphabet.

We then use a for loop to iterate over each character in the string. The `enumerate` function is used to get both the index and the character itself. We convert the character to lowercase using the `lower` method and compare it to the corresponding character in the English alphabet using the `chr` and `ord` functions. If the characters match, we increment the `count` variable.

Finally, we return the `count` variable as the result of the function. The `assert` statement is used to verify that the function returns the expected result for the given example.