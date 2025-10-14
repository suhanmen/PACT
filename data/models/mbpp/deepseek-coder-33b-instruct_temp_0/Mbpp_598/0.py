Here is the Python function to check whether the given number is an Armstrong number or not:

```python
def armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return n == sum

print(armstrong_number(153))  # Output: True
```

This function works by first initializing a variable `sum` to 0. It then enters a while loop, which continues until `temp` (a copy of `n`) is 0. In each iteration of the loop, it calculates the remainder of `temp` divided by 10 (which gives the last digit of `temp`), raises that digit to the power of 3, and adds the result to `sum`. It then divides `temp` by 10 (which effectively removes the last digit from `temp`). Finally, it checks if `n` is equal to `sum`, and returns the result. If `n` is equal to `sum`, that means `n` is an Armstrong number, so the function returns `True`; otherwise, it returns `False`.
