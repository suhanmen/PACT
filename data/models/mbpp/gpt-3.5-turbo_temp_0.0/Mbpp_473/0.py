Here is the completed code snippet:

```python
def tuple_intersection(tuple_list1, tuple_list2):
    set1 = set(tuple_list1)
    set2 = set(tuple_list2)
    intersection = set1.intersection(set2)
    return intersection

assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
```

The `tuple_intersection` function takes two tuple lists as input. It converts each list into a set to remove any duplicate tuples. Then, it finds the intersection of the two sets using the `intersection` method. Finally, it returns the intersection as a set.

The `assert` statement checks if the output of the `tuple_intersection` function matches the expected result, and raises an error if they are not equal. In this case, the expected result is `{(4, 5), (3, 4), (5, 6)}`.