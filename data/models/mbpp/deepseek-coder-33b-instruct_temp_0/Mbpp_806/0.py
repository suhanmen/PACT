Here is the Python function to find the maximum run of uppercase characters in the given string:

```python
def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for char in s:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run
```

You can test the function with the following code:

```python
print(max_run_uppercase('GeMKSForGERksISBESt'))  # Output: 5
```

This function works by iterating over each character in the string. If the character is uppercase, it increments the current run of uppercase characters. If the character is not uppercase, it resets the current run to 0. It also keeps track of the maximum run of uppercase characters seen so far.
