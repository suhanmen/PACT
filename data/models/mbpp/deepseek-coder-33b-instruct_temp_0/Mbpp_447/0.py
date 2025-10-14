Here is the Python function to find cubes of individual elements in a list:

```python
def cube_nums(nums):
    return [num ** 3 for num in nums]
```

You can test this function with the following code:

```python
print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
```

This should output:

```python
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```
