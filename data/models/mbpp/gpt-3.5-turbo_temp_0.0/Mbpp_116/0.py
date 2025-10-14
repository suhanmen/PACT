Here is the completed code snippet:

```python
def tuple_to_int(t):
    # Convert each element in the tuple to a string
    str_nums = [str(num) for num in t]
    
    # Join the string elements together and convert to an integer
    result = int(''.join(str_nums))
    
    return result

# Test the function
assert tuple_to_int((1,2,3)) == 123
```