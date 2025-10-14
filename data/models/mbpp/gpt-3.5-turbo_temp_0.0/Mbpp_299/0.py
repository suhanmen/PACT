Here is the completed code snippet:

```python
def max_aggregate(lst):
    aggregate = {}
    for name, score in lst:
        if name in aggregate:
            aggregate[name] += score
        else:
            aggregate[name] = score
    max_name = max(aggregate, key=aggregate.get)
    max_score = aggregate[max_name]
    return (max_name, max_score)

assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]) == ('Juan Whelan', 212)
```

The `max_aggregate` function takes a list of tuples as input. Each tuple contains a name and a score. The function calculates the aggregate score for each name and returns the name with the maximum aggregate score.

In the function, we initialize an empty dictionary `aggregate` to store the aggregate scores for each name. We iterate over each tuple in the input list and update the aggregate score for the corresponding name in the dictionary. If the name is already present in the dictionary, we add the score to the existing aggregate score. If the name is not present, we add a new entry to the dictionary with the score as the initial aggregate score.

After calculating the aggregate scores for all names, we use the `max` function with the `key` parameter set to `aggregate.get` to find the name with the maximum aggregate score. We then retrieve the maximum score from the dictionary using the name as the key.

Finally, we return a tuple containing the name and the maximum score. The `assert` statement is used to verify that the function returns the expected result for the given input.