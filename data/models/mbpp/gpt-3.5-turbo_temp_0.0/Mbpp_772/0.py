Here is the completed code snippet:

```python
def remove_length(string, k):
    words = string.split()
    filtered_words = [word for word in words if len(word) != k]
    return ' '.join(filtered_words)

assert remove_length('The person is most value tet', 3) == 'person is most value'
```

In this code, the `remove_length` function takes two parameters: `string` and `k`. It splits the string into a list of words using the `split()` method. Then, it filters out the words with length `k` using a list comprehension. Finally, it joins the filtered words back into a string using the `join()` method with a space as the separator. The resulting string is returned as the output.