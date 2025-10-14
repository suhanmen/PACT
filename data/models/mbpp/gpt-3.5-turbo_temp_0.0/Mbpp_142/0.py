Here is the completed code snippet:

```python
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count

assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]) == 3
```

The `count_samepair` function takes three lists as input and initializes a count variable to 0. It then iterates over the indices of the lists using a for loop. If the elements at the current index in all three lists are equal, the count is incremented by 1. Finally, the function returns the count.

The assert statement at the end of the code snippet verifies that the function produces the expected result for the given example.