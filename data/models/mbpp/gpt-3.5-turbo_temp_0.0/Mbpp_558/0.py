Here is the completed code snippet:

```python
def digit_distance_nums(num1, num2):
    sum = 0
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        sum += abs(digit1 - digit2)
        num1 //= 10
        num2 //= 10
    return sum

assert digit_distance_nums(1, 2) == 1
```

In this code, the `digit_distance_nums` function takes two integers as input and calculates the sum of the per-digit difference between them. It uses a while loop to iterate through each digit of the numbers. The modulus operator `%` is used to get the last digit of each number, and the absolute difference between the digits is added to the `sum` variable. The integer division operator `//` is used to remove the last digit from each number. Finally, the function returns the sum. The assert statement is used to verify that the function returns the expected result.