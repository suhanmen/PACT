Here is the completed code snippet:

```python
def neg_nos(numbers):
    negative_numbers = []
    for num in numbers:
        if num < 0:
            negative_numbers.append(num)
    return negative_numbers

assert neg_nos([-1, 4, 5, -6]) == [-1, -6]
```

The `neg_nos` function takes a list of numbers as input and returns a new list containing only the negative numbers from the input list. The function iterates over each number in the input list and checks if it is less than 0. If it is, the number is appended to the `negative_numbers` list. Finally, the function returns the `negative_numbers` list.

The `assert` statement at the end of the code snippet is used to verify that the function behaves as expected. It checks if the output of the `neg_nos` function, when called with the input `[-1, 4, 5, -6]`, is equal to the expected output `[-1, -6]`. If the condition is true, the code continues execution. If the condition is false, an `AssertionError` is raised.