Here is the Python function implemented in a markdown style code block:

```python
def overlapping(seq1, seq2):
    """
    This function checks whether any value in a sequence exists in another sequence or not.
    """
    for i in seq1:
        if i in seq2:
            return True
    return False
```

You can use this function to check if any value in the first sequence exists in the second sequence. Here is an example of how to use it:

```python
print(overlapping([1,2,3,4,5],[6,7,8,9]))  # Output: False
```

In this example, the function `overlapping` is called with two sequences `[1,2,3,4,5]` and `[6,7,8,9]`. The function checks if any value in the first sequence exists in the second sequence. Since no value in the first sequence exists in the second sequence, the function returns `False`.
