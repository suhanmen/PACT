Here is the completed code snippet:

```python
def perfect_squares(start, end):
    squares = []
    for num in range(start, end+1):
        if num**0.5 == int(num**0.5):
            squares.append(num)
    return squares

assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
```

The `perfect_squares` function takes in two parameters, `start` and `end`, which represent the range of numbers to check for perfect squares. It initializes an empty list called `squares` to store the perfect squares found.

The function then iterates over each number in the range from `start` to `end+1`. For each number, it checks if the square root of the number is an integer. If it is, it means the number is a perfect square, so it is appended to the `squares` list.

Finally, the function returns the `squares` list containing all the perfect squares found within the given range.

The `assert` statement at the end of the code snippet verifies that the function returns the expected result when called with the given example input.