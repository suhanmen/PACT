Here is the completed code snippet:

```python
def reverse_words(string):
    words = string.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

assert reverse_words("python program") == "program python"
```