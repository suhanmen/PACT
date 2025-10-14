Here is the completed code snippet:

```python
def count_integer(lst):
    count = 0
    for element in lst:
        if isinstance(element, int):
            count += 1
    return count

assert count_integer([1,2,'abc',1.2]) == 2
```

The `count_integer` function takes a list as input and initializes a count variable to 0. It then iterates over each element in the list and checks if the element is an instance of the `int` class using the `isinstance` function. If the element is an integer, the count is incremented by 1. Finally, the function returns the count.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given example input.