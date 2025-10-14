Here's the completed code snippet:

```python
def is_undulating(num):
    num_str = str(num)
    if len(num_str) < 3:
        return False
    for i in range(1, len(num_str) - 1):
        if num_str[i] == num_str[i-1] and num_str[i] == num_str[i+1]:
            return False
        if num_str[i] != num_str[i-1] and num_str[i] != num_str[i+1]:
            return False
    return True

assert is_undulating(1212121) == True
```

The `is_undulating` function takes a number as input and converts it to a string. It then checks if the length of the string is less than 3, in which case it returns False since an undulating number must have at least 3 digits.

Next, it iterates through the string from the second digit to the second-to-last digit. For each digit, it checks if it is equal to both the previous and next digits. If it is, then it is not an undulating number and False is returned. If it is not equal to either the previous or next digit, then it is also not an undulating number and False is returned.

If the function has not returned False at any point, it means that the number is undulating and True is returned.

The assert statement at the end checks if the function returns True for the given example input of 1212121.