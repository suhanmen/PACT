Here is the Python function to count the number of equal numbers from three given integers:

```python
def test_three_equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0
```

This function works by first checking if all three numbers are equal. If they are, it returns 3. If not, it checks if any two numbers are equal. If they are, it returns 2. If neither of these conditions are met, it returns 0.
