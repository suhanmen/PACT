Here is the completed code snippet:

```python
def len_log(words):
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length

assert len_log(["python","PHP","bigdata"]) == 7
```

The `len_log` function takes a list of words as input and iterates through each word to find the length of the longest word. It initializes a variable `longest_length` to 0 and updates it if a longer word is found. Finally, it returns the `longest_length`. The `assert` statement is used to verify that the function returns the expected result.