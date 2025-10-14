Here is the completed code snippet:

```python
def upper_ctr(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

assert upper_ctr('PYthon') == 1
```