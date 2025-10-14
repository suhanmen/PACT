Here is the completed code snippet:

```python
def is_Sum_Of_Powers_Of_Two(num):
    if num <= 0:
        return False
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num -= 1
        if num == 0:
            return True
    return False

assert is_Sum_Of_Powers_Of_Two(10) == True
```

This function checks whether the given number can be represented as the sum of non-zero powers of 2. It starts by checking if the number is less than or equal to 0, in which case it returns False. Then, it enters a loop where it repeatedly divides the number by 2 if it is even, or subtracts 1 if it is odd. If the number eventually becomes 0, it means that it can be represented as the sum of non-zero powers of 2, so the function returns True. If the loop finishes without the number becoming 0, it means that it cannot be represented as the sum of non-zero powers of 2, so the function returns False.