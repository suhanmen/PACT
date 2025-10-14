Here is the completed code snippet:

```python
def max_run_uppercase(string):
    max_run = 0
    current_run = 0

    for char in string:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run

assert max_run_uppercase('GeMKSForGERksISBESt') == 5
```