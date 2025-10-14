Here is the Python function to find the median of two sorted lists of same size:

```python
def get_median(arr1, arr2, n):
    if n <= 0:
        return -1
    elif n == 1:
        return (arr1[0]+arr2[0])/2
    elif n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)

        if m1 > m2:
            if n % 2 == 0:
                return get_median(arr1[:n//2+1], arr2[n//2:], n//2 + 1)
            else:
                return get_median(arr1[:n//2+1], arr2[n//2:], n//2 + 1)
        else:
            if n % 2 == 0:
                return get_median(arr1[n//2-1:], arr2[:n//2+1], n//2 + 1)
            else:
                return get_median(arr1[n//2:], arr2[:n//2+1], n//2 + 1)

def median(arr, n):
    if n % 2 == 0:
        return (arr[n//2] + arr[n//2-1]) / 2
    else:
        return arr[n//2]
```

This function works by recursively dividing the lists in half and comparing the medians of the two lists. It then discards the half of the list that does not contain the median, and repeats the process until it finds the median.

The median function is a helper function that calculates the median of a list.

Please note that this function assumes that the input lists are sorted in ascending order. If the input lists are not sorted, the function may not work correctly.
