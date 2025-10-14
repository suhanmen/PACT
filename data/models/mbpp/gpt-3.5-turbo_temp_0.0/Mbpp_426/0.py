Here is the completed code snippet:

```python
def filter_oddnumbers(numbers):
    return [num for num in numbers if num % 2 != 0]

assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
```

The function `filter_oddnumbers` takes a list of numbers as input and uses a list comprehension to filter out the odd numbers. It checks if each number in the input list is not divisible by 2 (i.e., it is odd) and adds it to a new list. Finally, it returns the new list containing only the odd numbers.

The `assert` statement is used to verify that the function returns the expected output. In this case, it checks if `filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])` returns `[1, 3, 5, 7, 9]`, and if not, it raises an `AssertionError`.