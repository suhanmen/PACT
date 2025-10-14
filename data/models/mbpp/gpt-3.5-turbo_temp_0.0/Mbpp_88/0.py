Here is the completed code snippet:

```python
def freq_count(lst):
    freq_dict = {}
    for element in lst:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    return freq_dict

assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]) == {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
```

The `freq_count` function takes a list as input and initializes an empty dictionary `freq_dict` to store the frequency of each element. It then iterates over each element in the list and checks if it already exists as a key in the dictionary. If it does, it increments the value by 1. If it doesn't, it adds the element as a key with a value of 1. Finally, it returns the `freq_dict` dictionary.