Here is the Python function that solves the problem:

```python
def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]
```

This function uses the built-in `min` function in Python, which returns the smallest item in an iterable or the smallest of two or more arguments. The `key` argument specifies a one-argument ordering function like that used for list.sort(). The `min` function will return the tuple with the smallest second value, and then we return the first value of that tuple using `[0]`.

You can test the function with the provided example:

```python
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]))  # Output: 'Varsha'
```
