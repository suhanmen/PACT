Here is the completed code snippet:

```python
def Split(lst):
    return [num for num in lst if num % 2 != 0]

assert Split([1,2,3,4,5,6]) == [1,3,5]
```

The function `Split` takes a list `lst` as input and uses a list comprehension to filter out the even numbers. It checks if each number in the list is odd by using the modulo operator `%` to check if the number is divisible by 2. If the number is not divisible by 2 (i.e., it is odd), it is included in the resulting list. Finally, the function returns the resulting list of odd numbers.

The `assert` statement is used to verify that the function returns the expected output. In this case, it checks if `Split([1,2,3,4,5,6])` returns `[1,3,5]`. If the assertion fails, an `AssertionError` will be raised.