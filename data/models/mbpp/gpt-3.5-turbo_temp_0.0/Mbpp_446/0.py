Here is the completed code snippet:

```python
def count_Occurrence(tup, lst):
    count = 0
    for element in lst:
        count += tup.count(element)
    return count

assert count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3
```

In this code, the `count_Occurrence` function takes two arguments: `tup` (the tuple) and `lst` (the list of elements to count). 

The function initializes a variable `count` to 0. It then iterates over each element in the `lst` list and uses the `count` method of the `tup` tuple to count the occurrences of that element. The count is added to the `count` variable.

Finally, the function returns the total count.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks that `count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b'])` returns 3.