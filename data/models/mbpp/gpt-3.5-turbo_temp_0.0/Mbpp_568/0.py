Here is the completed code snippet:

```python
def empty_list(N):
    return [{} for _ in range(N)]

assert empty_list(5) == [{},{},{},{},{}]
```