Here is the Python function implemented in a markdown style code block:

```python
def max_aggregate(lst):
    """
    Write a function to calculate the maximum aggregate from the list of tuples.
    """
    # Create a dictionary to store the aggregate scores
    aggregate_scores = {}

    # Iterate over the list of tuples
    for name, score in lst:
        # If the name is already in the dictionary, add the score to the existing aggregate
        if name in aggregate_scores:
            aggregate_scores[name] += score
        # If the name is not in the dictionary, add it with the score as the aggregate
        else:
            aggregate_scores[name] = score

    # Find the name with the maximum aggregate score
    max_name = max(aggregate_scores, key=aggregate_scores.get)
    max_score = aggregate_scores[max_name]

    # Return the name and score as a tuple
    return (max_name, max_score)
```

You can test the function with the provided assertion:

```python
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
```

This function works by first creating a dictionary to store the aggregate scores for each name. It then iterates over the list of tuples, adding the score to the aggregate for each name. Finally, it finds the name with the maximum aggregate score and returns it as a tuple.
