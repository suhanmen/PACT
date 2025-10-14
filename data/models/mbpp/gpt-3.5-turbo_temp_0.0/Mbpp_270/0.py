Here is the completed code snippet:

```python
def sum_even_and_even_index(lst):
    # Initialize the sum variable
    total = 0
    
    # Iterate over the list and check if the number is even and its index is even
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 == 0:
            total += lst[i]
    
    # Return the sum
    return total

# Test the function
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
```