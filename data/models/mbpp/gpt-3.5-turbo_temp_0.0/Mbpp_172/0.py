Here is the completed code snippet:

```python
def count_occurance(string):
    count = 0
    index = 0
    while index < len(string):
        if string[index:index+3] == 'std':
            count += 1
            index += 3
        else:
            index += 1
    return count

assert count_occurance("letstdlenstdporstd") == 3
```