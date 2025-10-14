Here is the completed code snippet:

```python
def count_Substrings(string):
    count = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count

assert count_Substrings('112112') == 6
```

In this code, we define a function `count_Substrings` that takes a string as input. We initialize a variable `count` to keep track of the number of substrings that meet the condition.

We use two nested loops to iterate through all possible substrings of the input string. The outer loop iterates over the starting index of the substring, and the inner loop iterates over the ending index of the substring.

For each substring, we calculate the sum of its digits using a generator expression and the `sum` function. We then compare this sum to the length of the substring. If they are equal, we increment the `count` variable.

Finally, we return the `count` variable as the result of the function.

The `assert` statement at the end of the code snippet verifies that the function produces the expected result for the given example input.