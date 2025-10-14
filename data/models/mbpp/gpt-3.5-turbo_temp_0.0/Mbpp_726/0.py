Here is the completed code snippet:

```python
def multiply_elements(numbers):
    result = ()
    for i in range(len(numbers) - 1):
        result += (numbers[i] * numbers[i+1],)
    return result

assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
```

The function `multiply_elements` takes a tuple of numbers as input. It iterates over the elements of the tuple, multiplying each element with the next element and adding the result to a new tuple `result`. Finally, it returns the `result` tuple.

The `assert` statement checks if the function returns the expected result for the given input tuple.