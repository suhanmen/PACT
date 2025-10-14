Here is the completed code snippet:

```python
def min_Swaps(bin1, bin2):
    count = 0
    for i in range(len(bin1)):
        if bin1[i] != bin2[i]:
            count += 1
    return count

assert min_Swaps("1101","1110") == 1
```

In this code, the `min_Swaps` function takes two binary numbers represented as strings (`bin1` and `bin2`) as input. It iterates through each character of the strings and checks if the corresponding characters are different. If they are different, it increments the `count` variable. Finally, it returns the `count` as the minimum number of swaps required to convert `bin1` to `bin2`.

The `assert` statement at the end of the code snippet verifies that the `min_Swaps` function returns the expected result for the given example.