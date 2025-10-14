def largest_smallest_integers(lst):
    negatives = [i for i in lst if i < 0]
    positives = [i for i in lst if i > 0]
    if not negatives:
        largest = None
    else:
        largest = max(negatives)
    if not positives:
        smallest = None
    else:
        smallest = min(positives)
    return (largest, smallest)
