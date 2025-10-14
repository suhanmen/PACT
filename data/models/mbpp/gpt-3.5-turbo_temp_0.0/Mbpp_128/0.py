Here is the completed code snippet:

```python
def long_words(n, sentence):
    words = sentence.split()
    long_words = []
    for word in words:
        if len(word) > n:
            long_words.append(word)
    return long_words

assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
```

In this code, the `long_words` function takes two parameters: `n` (the minimum length of words to consider) and `sentence` (the input sentence). 

The sentence is split into individual words using the `split()` method. Then, each word is checked to see if its length is greater than `n`. If it is, the word is added to the `long_words` list.

Finally, the `long_words` list is returned as the result. The `assert` statement is used to verify that the function produces the expected output.