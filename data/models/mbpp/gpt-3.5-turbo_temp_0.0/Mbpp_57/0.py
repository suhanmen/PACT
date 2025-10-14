Here is the completed code snippet:

```python
def find_Max_Num(digits):
    # Sort the digits in descending order
    digits.sort(reverse=True)
    
    # Convert the sorted digits to a string
    num_str = ''.join(map(str, digits))
    
    # Convert the string to an integer
    max_num = int(num_str)
    
    return max_num

# Test the function
assert find_Max_Num([1,2,3]) == 321
```

In this code, we first sort the digits in descending order using the `sort()` method with the `reverse=True` parameter. Then, we convert the sorted digits to a string using the `join()` method and `map()` function. Finally, we convert the string to an integer using the `int()` function and return the result.