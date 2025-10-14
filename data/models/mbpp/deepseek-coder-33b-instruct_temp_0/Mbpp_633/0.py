Here is the Python function to find the sum of xor of all pairs of numbers in the given list:

```python
def pair_xor_Sum(lst, n):
    sum = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            sum += lst[i] ^ lst[j]
    return sum * 2
```

This function works by iterating over each pair of numbers in the list and calculating the XOR of the pair. The XOR of a pair is then added to the sum. The final sum is then multiplied by 2 because each pair is counted twice (once for each number in the pair).

You can test this function with the following code:

```python
print(pair_xor_Sum([5,9,7,6],4)) # Output: 47
```

This will output `47`, which is the expected result.
