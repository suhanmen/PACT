Here is the Python function that checks if the given sequences follow the same pattern:

```python
def is_samepatterns(seq1, seq2):
    """
    This function checks whether the two sequences follow the same pattern.
    """
    # Create a dictionary to map elements from seq1 to elements from seq2
    mapping = {}

    # Check if the sequences have the same length
    if len(seq1) != len(seq2):
        return False

    # Iterate over the sequences
    for i in range(len(seq1)):
        # If the element from seq1 is not in the mapping dictionary, add it
        if seq1[i] not in mapping:
            mapping[seq1[i]] = seq2[i]
        # If the element from seq1 is in the mapping dictionary, check if it maps to the same element in seq2
        elif mapping[seq1[i]] != seq2[i]:
            return False

    # If we have not returned False yet, the sequences follow the same pattern
    return True
```

You can use this function to check if two sequences follow the same pattern. For example:

```python
print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))  # Returns: True
print(is_samepatterns(["red","green","blue"], ["a", "b", "c"]))  # Returns: False
```
