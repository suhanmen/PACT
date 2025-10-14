Here is the completed code snippet:

```python
def find_tuples(lst, k):
    result = []
    for tup in lst:
        if all(elem % k == 0 for elem in tup):
            result.append(tup)
    return result

assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
```

The `find_tuples` function takes a list of tuples `lst` and a number `k` as input. It iterates over each tuple in the list and checks if all elements in the tuple are divisible by `k`. If so, the tuple is added to the `result` list. Finally, the function returns the `result` list.

The `assert` statement at the end verifies that the function returns the expected result. In this case, it checks if `find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6)` returns `[(6, 24, 12)]`.