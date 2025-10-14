Here is the completed code snippet:

```python
def dif_Square(num):
    for i in range(1, int(num**0.5) + 1):
        diff = num - i**2
        if diff >= 0 and int(diff**0.5)**2 == diff:
            return True
    return False

assert dif_Square(5) == True
```

In this code, we iterate through all the numbers from 1 to the square root of the given number. For each number, we calculate the difference between the given number and the square of the current number. If this difference is a perfect square, we return True. If no such difference is found, we return False.