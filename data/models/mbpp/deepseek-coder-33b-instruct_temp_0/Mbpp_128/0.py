Here is the Python function implemented in a markdown style code block:

```python
def long_words(n, sentence):
    """
    Write a function to find words that are longer than n characters from a given list of words.
    """
    words = sentence.split()
    long_words = [word for word in words if len(word) > n]
    return long_words

# Test the function
print(long_words(3,"python is a programming language"))
```

This function works by first splitting the input sentence into a list of words. It then uses a list comprehension to create a new list that only includes words that are longer than `n` characters. The function finally returns this new list.

The test at the end of the code block calls the function with the provided test case and prints the result.
