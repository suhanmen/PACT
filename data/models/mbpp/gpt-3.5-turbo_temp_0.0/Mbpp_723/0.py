Here is the completed code snippet:

```python
def count_same_pair(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]) == 4
```

The function `count_same_pair` takes two lists as input and initializes a count variable to 0. It then iterates over the indices of the lists using a for loop. If the values at the current index in both lists are the same, it increments the count variable. Finally, it returns the count.

The assert statement at the end of the code snippet verifies that the function produces the expected output for the given example.