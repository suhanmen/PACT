Here is the completed code snippet:

```python
def interleave_lists(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result

assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
```

The `interleave_lists` function takes three lists as input and iterates over them using a for loop. In each iteration, it appends the corresponding elements from each list to the `result` list. Finally, it returns the `result` list.

The `assert` statement is used to verify that the function produces the expected output.