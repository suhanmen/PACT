Here is the Python function to count bidirectional tuple pairs:

```python
def count_bidirectional(tuples):
    count = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            if tuples[i] == tuples[j][::-1]:
                count += 1
    return count
```

This function works by iterating over each pair of tuples in the list. If a pair is bidirectional (i.e., the first element of the first tuple is equal to the second element of the second tuple, and vice versa), it increments a counter. The function then returns the counter.

You can test this function with the following code:

```python
print(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]))  # Output: 3
```

This will output `3`, which is the expected result.
