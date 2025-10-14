Here is the completed code snippet:

```python
def is_majority(arr, n, element):
    count = 0
    for i in range(n):
        if arr[i] == element:
            count += 1
    return count > n/2

assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
```

In this code, we iterate through the array and count the occurrences of the given element. If the count is greater than n/2, we return True indicating that the element is the majority element. Otherwise, we return False. The assert statement is used to verify that the function returns the expected result.