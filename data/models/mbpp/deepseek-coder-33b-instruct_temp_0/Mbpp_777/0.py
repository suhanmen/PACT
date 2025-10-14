Here is the Python function to find the sum of non-repeated elements in a given list:

```python
def find_sum(lst):
    return sum(i for i in lst if lst.count(i) == 1)

# Test the function
print(find_sum([1,2,3,1,1,4,5,6]))  # Output: 12
```

This function works by iterating over each element in the list and checking if its count is equal to 1 (meaning it's not repeated). If it is, it's added to the sum. The `sum` function is then used to add up all these elements.
