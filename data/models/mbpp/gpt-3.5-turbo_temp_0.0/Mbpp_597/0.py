Here is the completed code snippet:

```python
def find_kth(arr1, arr2, k):
    # Merge the two sorted arrays
    merged = sorted(arr1 + arr2)
    
    # Return the kth element
    return merged[k-1]

assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
```

In this code, the `find_kth` function takes in two sorted arrays `arr1` and `arr2`, and an integer `k`. It merges the two arrays using the `sorted` function and stores the result in the `merged` variable. Then, it returns the kth element from the merged array by accessing the element at index `k-1`. Finally, the code includes an assertion to verify that the function returns the expected result.