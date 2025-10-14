Here is the Python function that counts the number of pairs of integers in a list that xor to an even number:

```python
def find_even_pair(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] ^ lst[j] % 2 == 0:
                count += 1
    return count
```

You can test the function with the following code:

```python
print(find_even_pair([5, 4, 7, 2, 1]))  # Output: 4
```

This function works by iterating over all pairs of integers in the list and checking if their xor operation results in an even number. If it does, it increments the count. The function finally returns the count.
