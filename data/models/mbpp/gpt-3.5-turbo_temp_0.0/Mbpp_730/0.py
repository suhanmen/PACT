Here is the completed code snippet:

```python
def consecutive_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            result.append(lst[i])
    return result

assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
```

The `consecutive_duplicates` function takes a list as input and returns a new list with consecutive duplicates removed. It iterates through the input list and checks if the current element is the same as the previous element. If it is not, the current element is appended to the result list. The function then returns the result list.

The `assert` statement at the end of the code snippet checks if the function produces the expected output for a given input list. If the output matches the expected result, the code will run without any errors.