Here is the completed code snippet:

```python
def find_Odd_Pair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] ^ arr[j]) % 2 != 0:
                count += 1
    return count

assert find_Odd_Pair([5,4,7,2,1],5) == 6
```

In this code, the function `find_Odd_Pair` takes an array `arr` and the length of the array `n` as input. It initializes a variable `count` to keep track of the number of pairs with odd xor values.

The function then uses nested loops to iterate through all possible pairs of elements in the array. For each pair, it calculates the xor value using the `^` operator. If the xor value is odd (i.e., not divisible by 2), it increments the `count` variable.

Finally, the function returns the `count` variable.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given example input.