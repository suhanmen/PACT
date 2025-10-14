Here is the completed code snippet:

```python
def multiple_to_single(lst):
    # Convert each integer in the list to a string
    str_lst = [str(num) for num in lst]
    
    # Join the strings together into a single string
    single_str = ''.join(str_lst)
    
    # Convert the single string back to an integer
    single_int = int(single_str)
    
    return single_int

# Test the function
assert multiple_to_single([11, 33, 50]) == 113350
```