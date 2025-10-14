Here is the completed code snippet:

```python
def remove_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

assert remove_odd([1,2,3]) == [2]
```

The `remove_odd` function takes a list of numbers as input and uses a list comprehension to filter out the odd numbers. It checks if each number in the list is divisible by 2 (i.e., even) using the modulo operator `%`. If the number is even, it is included in the new list. Finally, the function returns the new list with only the even numbers.

The `assert` statement is used to verify that the function behaves as expected. In this case, it checks if calling `remove_odd([1,2,3])` returns `[2]`, which is the expected output. If the assertion fails, an `AssertionError` will be raised.