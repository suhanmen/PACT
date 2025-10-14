Here is the completed code snippet:

```python
def square_nums(nums):
    return [num**2 for num in nums]

assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

The `square_nums` function takes a list of numbers as input and returns a new list with the squares of each individual element. The list comprehension `[num**2 for num in nums]` is used to iterate over each element in the input list `nums` and calculate its square using the exponentiation operator `**`. The resulting list of squares is then returned. The `assert` statement is used to verify that the function produces the expected output.