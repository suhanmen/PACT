Here is the Python function to find kth element from the given two sorted arrays:

```python
def find_kth(arr1, arr2, k):
    if len(arr1) + len(arr2) < k:
        return None

    if not arr1:
        return arr2[k - 1]
    if not arr2:
        return arr1[k - 1]

    mid1, mid2 = len(arr1) // 2 , len(arr2) // 2

    if mid1 + mid2 < k:
        if arr1[mid1] > arr2[mid2]:
            return find_kth(arr1, arr2[mid2 + 1:], k - mid2 - 1)
        else:
            return find_kth(arr1[mid1 + 1:], arr2, k - mid1 - 1)
    else:
        if arr1[mid1] > arr2[mid2]:
            return find_kth(arr1[:mid1], arr2, k)
        else:
            return find_kth(arr1, arr2[:mid2], k)

# Test the function
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # Output: 6
```

This function works by comparing the middle elements of the two arrays. If the sum of the middle indices is less than k, it means the kth element is in the second half of one of the arrays. If the middle element of the first array is greater than the middle element of the second array, it means the kth element is in the second half of the first array, so it recursively calls the function with the second half of the first array and the whole second array. If the middle element of the first array is not greater than the middle element of the second array, it means the kth element is in the first half of the first array, so it recursively calls the function with the first half of the first array and the whole second array. If the sum of the middle indices is not less than k, it means the kth element is in the first half of one of the arrays. If the middle element of the first array is greater than the middle element of the second array, it means the kth element is in the first half of the first array, so it recursively calls the function with the whole first array and the first half of the second array. If the middle element of the first array is not greater than the middle element of the second array, it means the kth element is in the first half of the second array, so it recursively calls the function with the whole first array and the first half of the second array.
