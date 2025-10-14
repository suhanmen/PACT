Here is the completed code snippet:

```python
def count_first_elements(tup):
    count = 0
    for i in range(len(tup)):
        if isinstance(tup[i], tuple):
            break
        count += 1
    return count

assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
```

In this code, the function `count_first_elements` takes a tuple as input and counts the number of elements that occur before the first tuple element. It iterates through the tuple using a for loop and checks if each element is an instance of a tuple using the `isinstance()` function. If it encounters a tuple element, it breaks out of the loop. The count is incremented for each non-tuple element encountered. Finally, the count is returned as the result.

The assert statement at the end of the code verifies that the function returns the expected result for the given example tuple.