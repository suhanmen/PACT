Here is the Python function to count the number of pairs whose xor value is odd.

```python
def find_Odd_Pair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] ^ arr[j]) & 1:
                count += 1
    return count
```

This function works by iterating over each pair of elements in the array and checking if the XOR of the pair is odd. If it is, it increments a counter. The function finally returns the count of such pairs.

The XOR operation is used to find the bitwise XOR of the pair, and the bitwise AND operation with 1 is used to check if the result is odd. If the result is odd, the bitwise AND operation will return 1, otherwise it will return 0.

You can test the function with the following code:

```python
print(find_Odd_Pair([5,4,7,2,1],5))  # Output: 6
```

This will output 6, which is the expected result.
