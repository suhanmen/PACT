Here is the completed code snippet:

```python
def highest_Power_of_2(n):
    power = 0
    while 2 ** power <= n:
        power += 1
    return 2 ** (power - 1)

assert highest_Power_of_2(10) == 8
```

This function uses a while loop to find the highest power of 2 that is less than or equal to the given number `n`. It starts with `power = 0` and keeps increasing `power` until `2 ** power` exceeds `n`. Finally, it returns `2 ** (power - 1)` to get the highest power of 2 that is less than or equal to `n`. The `assert` statement is used to verify that the function returns the expected result.