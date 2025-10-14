Here is the completed code snippet:

```python
def sort_numeric_strings(lst):
    return sorted(map(int, lst))

assert sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']) == [-500, -12, 0, 4, 7, 12, 45, 100, 200]
```

In this code, the `sort_numeric_strings` function takes a list of strings as input. It uses the `map` function to convert each string element to an integer using the `int` function. Then, the `sorted` function is used to sort the list of integers in ascending order. The sorted list is returned as the output. The `assert` statement is used to verify that the function produces the expected output.