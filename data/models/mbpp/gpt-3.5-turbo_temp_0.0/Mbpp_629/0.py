Here is the completed code snippet:

```python
def Split(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

assert Split([1,2,3,4,5]) == [2,4]
```

The `Split` function takes a list of numbers as input and returns a new list containing only the even numbers from the input list. It iterates over each number in the input list and checks if it is divisible by 2 (i.e., if it is even). If a number is even, it is added to the `even_numbers` list. Finally, the function returns the `even_numbers` list.

The `assert` statement at the end of the code snippet checks if the function produces the expected output for the given input. In this case, it checks if `Split([1,2,3,4,5])` returns `[2,4]`. If the assertion fails, an error will be raised.