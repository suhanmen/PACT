Here is the Python function to count the number of substrings with the sum of digits equal to their length:

```python
def count_Substrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        sum_digit = 0
        for j in range(i, n):
            sum_digit += int(s[j])
            if sum_digit == (j - i + 1):
                count += 1
    return count
```

You can test the function with the following code:

```python
print(count_Substrings('112112'))  # Output: 6
```

This function works by iterating over each character in the string and then for each character, it iterates over the remaining characters to form substrings. For each substring, it calculates the sum of digits and checks if it is equal to the length of the substring. If it is, it increments the count. The function finally returns the count.
