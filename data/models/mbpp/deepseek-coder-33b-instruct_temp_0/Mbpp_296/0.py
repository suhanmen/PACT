Here is the Python function to count inversions in an array:

```python
def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] > arr[j]):
                inv_count += 1
    return inv_count
```

You can test the function with the following code:

```python
print(get_Inv_Count([1,20,6,4,5]))  # Output: 5
```

This function works by iterating over each element in the array and comparing it with every element that comes after it. If it finds an element that is smaller than the current element, it increments the inversion count. The final inversion count is then returned.
