Here is the completed code snippet:

```
def sum_of_digits(numbers):
    sum_digits = 0
    for number in numbers:
        sum_digits += sum(int(digit) for digit in str(number))
    return sum_digits

assert sum_of_digits([10, 2, 56]) == 14
```

In this code, the `sum_of_digits` function takes a list of numbers as input. It initializes a variable `sum_digits` to keep track of the sum of digits. Then, it iterates over each number in the list. For each number, it converts it to a string and then iterates over each digit in the string. It converts each digit back to an integer and adds it to the `sum_digits` variable. Finally, it returns the total sum of digits.

The `assert` statement at the end is used to verify that the function produces the expected result for the given example.