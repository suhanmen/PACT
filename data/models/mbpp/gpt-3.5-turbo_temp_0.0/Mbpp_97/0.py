Here is the completed code snippet:

```python
def frequency_lists(lst):
    freq_dict = {}
    for sublist in lst:
        for element in sublist:
            if element in freq_dict:
                freq_dict[element] += 1
            else:
                freq_dict[element] = 1
    return freq_dict

assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
```

The `frequency_lists` function takes a list of lists as input and returns a dictionary where the keys are the elements in the flattened list and the values are the frequencies of each element. The function iterates over each sublist in the input list and then iterates over each element in the sublist. It checks if the element is already in the `freq_dict` dictionary and if so, increments its value by 1. If the element is not in the dictionary, it adds it as a new key with a value of 1. Finally, the function returns the `freq_dict` dictionary.