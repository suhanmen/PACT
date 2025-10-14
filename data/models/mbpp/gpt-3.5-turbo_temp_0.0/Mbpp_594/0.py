Here is the completed code snippet:

```python
def diff_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0 and even is None:
            even = num
        elif num % 2 != 0 and odd is None:
            odd = num
        if even is not None and odd is not None:
            break
    return even - odd

assert diff_even_odd([1,3,5,7,4,1,6,8]) == 3
```