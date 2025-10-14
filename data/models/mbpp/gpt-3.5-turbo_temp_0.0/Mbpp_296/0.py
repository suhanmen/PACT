Here is the completed code snippet:

```python
def get_Inv_Count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

assert get_Inv_Count([1,20,6,4,5]) == 5
```

The function `get_Inv_Count` takes an array as input and counts the number of inversions in the array. It uses two nested loops to compare each pair of elements in the array. If the first element is greater than the second element, it means there is an inversion and the count is incremented. Finally, the function returns the count of inversions.

The `assert` statement is used to verify that the function returns the expected result for the given input. In this case, it checks if the count of inversions in the array `[1,20,6,4,5]` is equal to 5.