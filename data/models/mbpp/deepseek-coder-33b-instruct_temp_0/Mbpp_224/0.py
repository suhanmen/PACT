Here is the Python function to count the number of set bits in a given number:

```python
def count_Set_Bits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
```

You can test the function with the following code:

```python
print(count_Set_Bits(2))  # Output: 1
```

This function works by using bitwise AND operation (`n & 1`) to check the least significant bit of the number. If the least significant bit is 1, it increments the count. Then it right shifts the number by 1 bit (`n >>= 1`) to check the next bit. This process continues until all bits have been checked.
