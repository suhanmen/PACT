Here is the Python function to find the sum of all odd length subarrays:

```python
def odd_length_sum(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        total += ((i+1) * (n-i) + 1) // 2 * arr[i]
    return total
```

This function works by iterating over each element in the array and calculating the number of subarrays that include that element. The number of subarrays that include an element is equal to the number of subarrays that start at that element plus the number of subarrays that end at that element. The number of subarrays that start at an element is equal to the index of that element plus one, and the number of subarrays that end at an element is equal to the length of the array minus the index of that element. The sum of these two numbers is the total number of subarrays that include that element.

The formula `(i+1) * (n-i) + 1) // 2` calculates the total number of subarrays that include the element at index `i`. The `// 2` operation is used to round down to the nearest integer, because the number of subarrays is always an integer.

Finally, the function multiplies the number of subarrays by the value of the element and adds this to the total.

The time complexity of this function is O(n), where n is the length of the array.
