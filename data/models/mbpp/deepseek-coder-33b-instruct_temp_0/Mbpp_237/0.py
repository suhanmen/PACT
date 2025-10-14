Here is the Python function that solves the problem:

```python
def check_occurences(tuples_list):
    # Create a dictionary to store the tuples and their counts
    tuples_dict = {}

    # Iterate over the list of tuples
    for tup in tuples_list:
        # If the tuple is already in the dictionary, increment its count
        if tup in tuples_dict:
            tuples_dict[tup] += 1
        # If the tuple is not in the dictionary, add it with a count of 1
        else:
            tuples_dict[tup] = 1

    # Return the dictionary
    return tuples_dict
```

This function works by iterating over the list of tuples and for each tuple, it checks if it is already in the dictionary. If it is, it increments the count for that tuple. If it is not, it adds the tuple to the dictionary with a count of 1. Finally, it returns the dictionary.
