Here is the completed code snippet:

```
def frequency(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count

assert frequency([1,2,3], 4) == 0
```