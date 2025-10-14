Here is the Python function implemented in a markdown style code block:

```python
def perfect_squares(start, end):
    result = []
    for i in range(start, end+1):
        if (i ** 0.5).is_integer():
            result.append(i)
    return result

print(perfect_squares(1,30))
```

This function works by iterating over each number in the range from `start` to `end` (inclusive). For each number, it checks if the square root of the number is an integer. If it is, the number is a perfect square and is added to the `result` list. The function finally returns this list.

When you run this code, it will print `[1, 4, 9, 16, 25]`, which are the perfect squares between 1 and 30.
