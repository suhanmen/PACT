Here is the Python function to remove all the words with k length in the given string:

```python
def remove_length(s, k):
    words = s.split()
    return ' '.join(word for word in words if len(word) != k)

print(remove_length('The person is most value tet', 3))
```

This function works by first splitting the input string into a list of words. Then it uses a generator expression to create a new list that includes only the words that are not of length `k`. Finally, it joins the words back into a single string with spaces in between.

The `print` statement at the end is used to test the function with the provided example.
