Here is the completed code snippet:

```python
def even_position(lst):
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            return False
    return True

assert even_position([3,2,1]) == False
```

The `even_position` function takes a list `lst` as input and iterates over the indices of the list using a for loop. It checks if the index `i` is even (i.e., divisible by 2) and if the corresponding element `lst[i]` is not even (i.e., not divisible by 2). If this condition is met, the function returns `False` to indicate that not every even index contains an even number. If the loop completes without finding any such case, the function returns `True` to indicate that every even index contains an even number.

The `assert` statement at the end of the code snippet checks if the function behaves as expected by comparing its output for the given input `[3,2,1]` with the expected output `False`.