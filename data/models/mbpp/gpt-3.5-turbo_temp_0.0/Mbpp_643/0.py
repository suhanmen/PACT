Here is the completed code snippet:

```python
def text_match_wordz_middle(word):
    if 'z' in word[1:-1]:
        return True
    else:
        return False

assert text_match_wordz_middle("pythonzabc.") == True
```