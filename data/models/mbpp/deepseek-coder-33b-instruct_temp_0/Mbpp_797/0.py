Here is the Python function implemented in a markdown style code block:

```python
def sum_in_range(l, r):
    sum = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            sum += i
    return sum
```

You can test the function with the following code:

```python
print(sum_in_range(2,5))  # Output: 8
```
