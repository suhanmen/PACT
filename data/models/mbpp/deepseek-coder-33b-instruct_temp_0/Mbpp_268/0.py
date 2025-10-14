Sure, here is the Python function to find the n'th star number:

```python
def find_star_num(n):
    count = 0
    num = 0
    while count < n:
        num += 1
        if str(num)[-1] == '6' and str(num)[0] == '5':
            count += 1
    return num
```

This function works by iterating over numbers starting from 1, and checking if the last digit of the number is 6 and the first digit is 5. If it is, it increments the count. When the count reaches n, it returns the current number.

Please note that this function will not work for large values of n, as it will take a long time to find the n'th star number. This is because star numbers are not uniformly distributed, and there are many numbers that are not star numbers.
