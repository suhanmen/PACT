Here is the completed code snippet:

```python
def start_withp(words):
    p_words = []
    for word in words:
        word_list = word.split()
        for w in word_list:
            if w.startswith('p') or w.startswith('P'):
                p_words.append(w)
    return tuple(p_words[:2])
```

This function takes a list of words as input and returns a tuple containing the first two words that start with the letter 'p' (case-insensitive). It splits each string in the list into individual words and checks if each word starts with 'p' or 'P'. If a word starts with 'p' or 'P', it is added to the `p_words` list. Finally, the function returns a tuple containing the first two words in the `p_words` list.