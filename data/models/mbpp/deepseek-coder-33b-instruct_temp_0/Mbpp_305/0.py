Here is the Python function that solves the problem:

```python
def start_withp(words):
    result = []
    for word in words:
        if word.startswith('p') or word.startswith('P'):
            result.append(word)
        if len(result) == 2:
            break
    return tuple(result)
```

This function iterates over the list of words and checks if the word starts with 'p' or 'P'. If it does, it adds the word to the result list. The function stops when it has found two words that start with 'p' or 'P'. The result is returned as a tuple.
