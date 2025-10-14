Here is the Python function that solves the problem:

```python
def larg_nnum(lst, n):
    lst.sort(reverse=True)
    return lst[:n]
```

This function works by first sorting the list in descending order (`reverse=True`) and then returning the first `n` elements of the sorted list.

You can test the function with the provided test case:

```python
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
```

This test case should pass without any assertion errors.
