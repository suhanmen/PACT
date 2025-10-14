Here is the Python function to check whether a list of numbers contains only one distinct element or not:

```python
def unique_Element(lst):
    return len(set(lst)) == 1

# Test the function
print(unique_Element([1,1,1])) # Expected output: True
```

In this function, we first convert the list to a set. In Python, a set is an unordered collection of unique elements. So, if all elements in the list are the same, the set will only contain one element. We then check if the length of the set is 1, which means the list contains only one distinct element.
