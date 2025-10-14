Here is the completed code snippet:

```python
def find_adverb_position(sentence):
    adverb = ""
    positions = []
    words = sentence.split()
    for i, word in enumerate(words):
        if word.endswith("ly"):
            adverb = word
            positions.append(i)
            break
    return tuple(positions + [adverb])

assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
```