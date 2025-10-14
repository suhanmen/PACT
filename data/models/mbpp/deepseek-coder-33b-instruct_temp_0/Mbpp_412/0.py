Here is the Python function to remove odd numbers from a given list:

```python
def remove_odd(num_list):
    return [num for num in num_list if num % 2 == 0]
```

This function uses list comprehension to iterate over each number in the input list. If the number is even (i.e., `num % 2 == 0`), it is included in the new list. If the number is odd, it is not included.
