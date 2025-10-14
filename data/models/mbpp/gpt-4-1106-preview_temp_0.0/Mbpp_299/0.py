"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""



def max_aggregate(scores):
    from collections import defaultdict
    aggregate_scores = defaultdict(int)
    for name, score in scores:
        aggregate_scores[name] += score
    return max(aggregate_scores.items(), key=lambda item: item[1])

# Example usage:
# assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]) == ('Juan Whelan', 212)
