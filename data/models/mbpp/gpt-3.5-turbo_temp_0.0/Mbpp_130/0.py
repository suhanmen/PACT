Here is the completed code snippet:

```python
def max_occurrences(lst):
    # Create a dictionary to store the frequency of each item
    freq_dict = {}
    
    # Iterate over the list and update the frequency dictionary
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    
    # Find the item with maximum frequency
    max_item = None
    max_freq = 0
    for item, freq in freq_dict.items():
        if freq > max_freq:
            max_item = item
            max_freq = freq
    
    return max_item

# Test the function
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2
```

The `max_occurrences` function takes a list as input and returns the item with the maximum frequency in the list. It uses a dictionary to store the frequency of each item in the list. Then, it iterates over the dictionary to find the item with the maximum frequency. Finally, it returns the item with the maximum frequency.