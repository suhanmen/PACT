Here is the Python function to sort a list of elements using Comb Sort algorithm:

```python
def comb_sort(lst):
    gap = len(lst)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(lst):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                sorted = False
            i += 1

    return lst
```

You can test the function with the provided example:

```python
print(comb_sort([5, 15, 37, 25, 79]))  # Output: [5, 15, 25, 37, 79]
```
