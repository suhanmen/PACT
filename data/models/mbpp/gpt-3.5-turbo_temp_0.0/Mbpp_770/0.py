Here is the completed code snippet:

```python
def odd_num_sum(n):
    sum = 0
    for i in range(1, 2*n+1, 2):
        sum += i**4
    return sum

assert odd_num_sum(2) == 82
```