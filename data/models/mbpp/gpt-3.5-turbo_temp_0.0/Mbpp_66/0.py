Here is the completed code snippet:

```python
def pos_count(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

assert pos_count([1,-2,3,-4]) == 2
```