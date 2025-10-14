Here is the completed code snippet:

```python
def similar_elements(list1, list2):
    return set(list1) & set(list2)

assert set(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) == set((4, 5))
```

The `similar_elements` function takes two lists as input and returns a set of the shared elements between the two lists. The `&` operator is used to find the intersection of the two sets created from the lists. The `assert` statement checks if the returned set is equal to the expected set `(4, 5)`.