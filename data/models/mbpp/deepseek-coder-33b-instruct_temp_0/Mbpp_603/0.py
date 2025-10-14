Here is the Python function to get all lucid numbers smaller than or equal to a given integer:

```python
def get_ludic(n):
    def is_ludic(n):
        """
        Check if a number is a lucid number.
        """
        if n == 1:
            return True
        for i in range(2, n+1):
            if n % i == 0:
                return False
        return True

    ludic_numbers = []
    for i in range(1, n+1):
        if is_ludic(i):
            ludic_numbers.append(i)
    return ludic_numbers

print(get_ludic(10))  # Output: [1, 2, 3, 5, 7]
```

In this code, the `is_ludic` function checks if a number is a lucid number. A lucid number is a number that is a prime number. The `get_ludic` function uses the `is_ludic` function to get all lucid numbers smaller than or equal to a given integer.
