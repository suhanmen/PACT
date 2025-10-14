Here is the completed code snippet:

```python
def difference(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    sum_of_numbers = sum(range(1, n+1))
    return sum_of_cubes - sum_of_numbers

assert difference(3) == 30
```