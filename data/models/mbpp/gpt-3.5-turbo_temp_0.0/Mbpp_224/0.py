Here is the completed code snippet:

```python
def count_Set_Bits(num):
    count = 0
    while num > 0:
        count += num & 1
        num >>= 1
    return count

assert count_Set_Bits(2) == 1
```

In this code, we use a while loop to iterate through each bit of the given number. We use the bitwise AND operator (`&`) with 1 to check if the least significant bit is set (i.e., equal to 1). If it is, we increment the count. Then, we right shift the number by 1 bit to move to the next bit. We repeat this process until the number becomes 0. Finally, we return the count.