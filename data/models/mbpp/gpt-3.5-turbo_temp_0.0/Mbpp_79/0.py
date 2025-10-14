Here is the completed code snippet:

```python
def word_len(word):
    if len(word) % 2 == 0:
        return False
    else:
        return True

assert word_len("Hadoop") == False
```

The `word_len` function takes a word as input and checks whether its length is odd or not. If the length is even, it returns `False`, otherwise it returns `True`. The `assert` statement is used to verify that the function returns the expected result for the given example.