Here is the Python function to find the highest power of 2 that is less than or equal to n:

```python
def highest_Power_of_2(n):
    res = 0
    for i in range(n, 0, -1):
        # If i is a power of 2
        if (i & (i - 1)) == 0:
            res = i
            break
    return res
```

You can test the function with the following code:

```python
print(highest_Power_of_2(10))  # Output: 8
```

This function works by iterating from n down to 1, checking each number to see if it is a power of 2. If it is, it sets that number as the result and breaks the loop. The function then returns the result.
