Here is the completed code snippet:

```python
def Find_Max(lst):
    max_length = 0
    max_element = None
    
    for element in lst:
        if len(element) > max_length:
            max_length = len(element)
            max_element = element
    
    return max_element

# Test case
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
```