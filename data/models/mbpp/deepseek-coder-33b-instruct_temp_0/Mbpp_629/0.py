Here is the Python function to find even numbers from a list of numbers:

```python
def find_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
```

You can use this function like this:

```python
print(find_even_numbers([1,2,3,4,5]))  # Output: [2, 4]
```

This function uses a list comprehension to iterate over each number in the input list. If a number is even (i.e., `num % 2 == 0`), it is included in the output list.
