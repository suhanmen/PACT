Here's the completed code snippet:

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

assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
```

The `comb_sort` function implements the comb sort algorithm to sort a list of elements. It starts with a large gap between elements and gradually reduces the gap until it becomes 1. In each iteration, it compares elements that are `gap` positions apart and swaps them if necessary. This process continues until the list is sorted.