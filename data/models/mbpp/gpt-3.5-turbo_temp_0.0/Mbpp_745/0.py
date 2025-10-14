Here is the completed code snippet:

```python
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        digits = [int(digit) for digit in str(num)]
        if all(num % digit == 0 for digit in digits):
            result.append(num)
    return result

assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
```

This function takes in a `startnum` and `endnum` as parameters and returns a list of numbers within that range where every number is divisible by every digit it contains. The function iterates through each number in the range and checks if every digit in the number divides the number evenly. If it does, the number is added to the result list. Finally, the function returns the result list. The provided assertion checks if the function produces the expected output for the given range.