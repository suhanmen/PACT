Here is the Python function for shell sort:

```python
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
```

You can test the function with the given array:

```python
print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))
```

This should output:

```python
[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
```
