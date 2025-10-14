Here is the Python function to sort a given list of strings of numbers numerically:

```python
def sort_numeric_strings(lst):
    return sorted(lst, key=int)

print(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']))
```

This function uses the built-in `sorted` function in Python, which sorts the elements of a list in a specific order (either ascending or descending). The `key` parameter of the `sorted` function specifies a function of one argument that is used to extract a comparison key from each element in the list. In this case, the `int` function is used to convert each string to an integer, which is then used as the comparison key.

The output of this function will be:

```python
['-500', '-12', '0', '4', '7', '12', '45', '100', '200']
```

Please note that the output is a list of strings, not integers. If you want the output to be a list of integers, you can modify the function as follows:

```python
def sort_numeric_strings(lst):
    return sorted(lst, key=int)

print(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']))
```

This will output:

```python
[-500, -12, 0, 4, 7, 12, 45, 100, 200]
```
