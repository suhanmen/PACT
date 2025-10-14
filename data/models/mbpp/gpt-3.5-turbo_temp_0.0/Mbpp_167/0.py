Here's the completed code snippet:

```python
def next_power_of_2(n):
    power = 0
    while 2 ** power < n:
        power += 1
    return 2 ** power

assert next_power_of_2(0) == 1
```

This function uses a while loop to find the smallest power of 2 that is greater than or equal to the given number `n`. It starts with `power` set to 0 and keeps increasing it until `2 ** power` is greater than or equal to `n`. Finally, it returns `2 ** power` as the result. The `assert` statement is used to verify that the function returns the expected result for the given test case.