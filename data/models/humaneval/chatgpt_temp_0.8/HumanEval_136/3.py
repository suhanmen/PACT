def largest_smallest_integers(lst):
    positives = [x for x in lst if x > 0]
    negatives = [x for x in lst if x < 0]
    if len(positives) == 0:
        b = None
    else:
        b = min(positives)
    if len(negatives) == 0:
        a = None
    else:
        a = max(negatives)
    return (a, b)
