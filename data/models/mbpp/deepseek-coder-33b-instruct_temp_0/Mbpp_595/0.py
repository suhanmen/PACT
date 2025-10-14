Here is the Python function to solve the problem:

```python
def min_Swaps(bin_str1, bin_str2):
    count = 0
    for i in range(len(bin_str1)):
        if bin_str1[i] != bin_str2[i]:
            count += 1
    return count // 2

print(min_Swaps("1101","1110"))
```

This function works by iterating over the characters in the two binary strings. If the characters at the same position in the two strings are not the same, it increments a counter. Finally, it returns the counter divided by 2, because each swap changes two characters.

Please note that this function assumes that the two binary strings are of the same length. If they are not, you would need to add additional error checking code to handle this case.
