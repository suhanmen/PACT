Here is the Python function to reverse words separated by spaces in a given string:

```python
def reverse_words(s):
    words = s.split(' ')
    reversed_words = ' '.join(reversed(words))
    return reversed_words
```

You can test the function with the following code:

```python
print(reverse_words("python program"))  # Output: "program python"
```

This function works by first splitting the input string into a list of words using the `split` method, then reversing the order of the words using the `reversed` function, and finally joining the reversed words back into a single string using the `join` method.
