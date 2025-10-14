Here is the completed code snippet:

```python
def list_split(lst, n):
    result = []
    for i in range(n):
        result.append(lst[i::n])
    return result

assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3) == [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
```

The `list_split` function takes in a list `lst` and an integer `n`. It initializes an empty list `result` to store the resulting lists. 

The function then iterates `n` times using a for loop, with the loop variable `i` ranging from 0 to `n-1`. 

Inside the loop, it uses list slicing with a step size of `n` to extract every `n`th element from the original list `lst`. The extracted elements are then appended to the `result` list.

Finally, the function returns the `result` list.

The assert statement at the end of the code snippet checks if the function produces the expected output for the given example.