Here is the completed code snippet:

```python
def overlapping(seq1, seq2):
    for value in seq1:
        if value in seq2:
            return True
    return False

assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
```